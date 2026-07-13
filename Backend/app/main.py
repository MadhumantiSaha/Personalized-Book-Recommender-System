from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.schemas import RecommendRequest, RecommendResponse, MetaResponse
from app.recommender import get_recommendations, get_categories, get_tones

app = FastAPI(title="Semantic Book Recommender API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/meta", response_model=MetaResponse)
def meta():
    return {"categories": get_categories(), "tones": get_tones()}

@app.post("/api/recommend", response_model=RecommendResponse)
def recommend(payload: RecommendRequest):
    if not payload.query.strip():
        raise HTTPException(status_code=400, detail="Query cannot be empty")
    results = get_recommendations(payload.query, payload.category, payload.tone)
    return {"results": results}

@app.get("/api/health")
def health():
    return {"status": "ok"}