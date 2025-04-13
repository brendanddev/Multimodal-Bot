"""
statistical_nlp.py

Brendan Dileo, April 2025
"""

import spacy
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nlp = spacy.load("en_core_web_md")
string = "I hear GitLab is great for aliens working on a project!"

def vectorize_utterance(utterance):
    texts = [string, utterance]

    # Count vectorizer
    count_vectorizer = CountVectorizer()
    count_vectors = count_vectorizer.fit_transform(texts)
    count_similarity = cosine_similarity(count_vectors[0:1], count_vectors[1:2]).flatten()[0]

    # Tfidf vectorizer
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_vectors = tfidf_vectorizer.fit_transform(texts)
    tfidf_similarity = cosine_similarity(tfidf_vectors[0:1], tfidf_vectors[1:2]).flatten()[0]

    print("\n--- Vector Similarity Results ---")
    print(f"CountVectorizer Similarity: {count_similarity:.4f}")
    print(f"TF-IDF Similarity:         {tfidf_similarity:.4f}")

if __name__ == "__main__":
    user_input = input("Enter a sentence to compare: ")
    vectorize_utterance(user_input)

