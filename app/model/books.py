import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def recommend_book(book):
    """Return a list of recommendations"""
    try:
        df = pd.read_csv("app/model/books.csv") # Load the dataset
        df["description"] = df["description"].fillna("") # Clear none

        vectorized = TfidfVectorizer(stop_words="english") # Vectorize the description
        vectorized_matrix = vectorized.fit_transform(df['description'])

        cosine = cosine_similarity(vectorized_matrix, vectorized_matrix) # Find similarity between the vectors
        titles = pd.Series(df["title"].index, index=df['title'].values) # Get the title as an index
        titles = titles[~titles.index.duplicated()] # Not touch duplicates
        search_title = titles[book] # Choose the book
        similar_score =pd.DataFrame(cosine[search_title], columns=["similar_score"]) # Similar books df
        book_similar = similar_score.sort_values("similar_score", ascending=False)[1:10] # Sort similar books

        return df["title"].loc[book_similar.index] # return books
    except Exception as e:
        print(f"An error occurred: {e}")
        return []