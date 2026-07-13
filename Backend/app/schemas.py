from pydantic import BaseModel
from typing import List

class RecommendRequest(BaseModel):
    query: str
    category: str = "All"
    tone: str = "All"

class Book(BaseModel):
    isbn13: str
    title: str
    authors: str
    description: str
    thumbnail: str
    category: str

class RecommendResponse(BaseModel):
    results: List[Book]

class MetaResponse(BaseModel):
    categories: List[str]
    tones: List[str]