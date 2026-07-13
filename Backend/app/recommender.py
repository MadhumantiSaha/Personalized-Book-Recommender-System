import pandas as pd
import numpy as np
from pathlib import Path

from langchain_community.document_loaders import TextLoader
# from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import CharacterTextSplitter
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()
BASE_DIR = Path(__file__).resolve().parent.parent  # Backend/app/


llm = ChatGroq(
    groq_api_key=os.environ.get("GROQ_API_KEY"),
    model="llama-3.3-70b-versatile",
)

def explain_recommendation(query: str, book_title: str, book_description: str) -> str:
    prompt = f"""In one short sentence, explain why the book "{book_title}" 
matches this request: "{query}"
Book description: {book_description}"""
    response = llm.invoke(prompt)
    return response.content


# books = pd.read_csv("books_with_emotions.csv")
books = pd.read_csv(BASE_DIR / "books_with_emotions.csv")

books["large_thumbnail"] = books["thumbnail"] + "&fife=w800"
books["large_thumbnail"] = np.where(
    books["large_thumbnail"].isna(),
    "cover-not-found.jpg",
    books["large_thumbnail"],
)

# raw_documents = TextLoader("tagged_description.txt", encoding="utf-8").load()
raw_documents = TextLoader(
    str(BASE_DIR / "tagged_description.txt"),
    encoding="utf-8",
    autodetect_encoding=True,
).load()
# raw_documents = TextLoader("tagged_description.txt").load()
# text_splitter = CharacterTextSplitter(separator="\n", chunk_size=0, chunk_overlap=0)
text_splitter = CharacterTextSplitter(separator="\n", chunk_size=1000, chunk_overlap=0)
documents = text_splitter.split_documents(raw_documents)


# db_books = Chroma.from_documents(documents, OpenAIEmbeddings())
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
db_books = Chroma.from_documents(documents, embedding_model)

def retrieve_semantic_recommendations(
        query: str,
        category: str = None,
        tone: str = None,
        initial_top_k: int = 50,
        final_top_k: int = 16,
) -> pd.DataFrame:

    recs = db_books.similarity_search(query, k=initial_top_k)
    books_list = [int(rec.page_content.strip('"').split()[0]) for rec in recs]
    book_recs = books[books["isbn13"].isin(books_list)].head(initial_top_k)

    if category and category != "All":
        book_recs = book_recs[book_recs["simple_categories"] == category].head(final_top_k)
    else:
        book_recs = book_recs.head(final_top_k)

    tone_map = {
        "Happy": "joy",
        "Surprising": "surprise",
        "Angry": "anger",
        "Suspenseful": "fear",
        "Sad": "sadness",
    }
    if tone in tone_map:
        book_recs = book_recs.sort_values(by=tone_map[tone], ascending=False)

    return book_recs


def format_authors(authors_field: str) -> str:
    authors_split = authors_field.split(";")
    if len(authors_split) == 2:
        return f"{authors_split[0]} and {authors_split[1]}"
    elif len(authors_split) > 2:
        return f"{', '.join(authors_split[:-1])}, and {authors_split[-1]}"
    return authors_field


def get_recommendations(query: str, category: str = "All", tone: str = "All"):
    recommendations = retrieve_semantic_recommendations(query, category, tone)
    results = []

    for _, row in recommendations.iterrows():
        description = row["description"]
        truncated_description = " ".join(description.split()[:30]) + "..."

        results.append({
            "isbn13": str(row["isbn13"]),
            "title": row["title"],
            "authors": format_authors(row["authors"]),
            "description": truncated_description,
            "thumbnail": row["large_thumbnail"],
            "category": row["simple_categories"],
        })
    return results


def get_categories():
    return ["All"] + sorted(books["simple_categories"].dropna().unique().tolist())


def get_tones():
    return ["All", "Happy", "Surprising", "Angry", "Suspenseful", "Sad"]