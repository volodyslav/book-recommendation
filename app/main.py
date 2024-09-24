from fastapi import FastAPI
from pydantic import BaseModel
from app.model.books import recommend_book

app = FastAPI()

class Book(BaseModel):
    title: str

@app.get("/")
def home():
    return {"message": "Welcome to the Book Recommender API"}

@app.post("/recommend")
def recommend_book_endpoint(book: Book):
    recommended_book = recommend_book(book.title)
    return {"recommended_book": recommended_book}
