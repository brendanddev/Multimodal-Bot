
"""
Statistical NLP with TF-IDF and Cosine Similarity for Intent Classification
Brendan Dileo
"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import random
import string

responses = {
    "greeting": ["Hello!", "Hi there!", "Hey! How's it going?"],
    "goodbye": ["Goodbye!", "See you later!", "Take care!"],
    "thank": ["You're welcome!", "No problem!", "Glad to help!"],
    "apology": ["No worries!", "It's okay!", "I understand."],
    "question": ["Hmm, let me think about that...", "That's a great question!", "Let me find out!"],
    "command": ["Okay, I'll try to do that!", "Got it, processing...", "I'll work on it."],
    "statement": ["Interesting! Tell me more.", "Oh, really?", "That makes sense."]
}

training_data = {
    "greeting": ["hello", "hi", "hey", "greetings", "morning", "good evening"],
    "goodbye": ["bye", "goodbye", "see you", "farewell", "take care"],
    "thank": ["thanks", "thank you", "appreciate it"],
    "apology": ["sorry", "apologize", "my bad", "pardon me"],
    "question": ["what", "how", "when", "where", "why", "is", "do", "can", "could", "would"],
    "command": ["give", "show", "tell", "bring", "help", "give me", "do"],
    "statement": ["I am", "it's", "this is", "they are", "there is", "was", "will be"]
}

def preprocess_input(user_input):
    user_input = user_input.translate(str.maketrans('', '', string.punctuation)).lower()
    return user_input

def classify_statistical_intent(user_input):
    user_input = preprocess_input(user_input) 
        
    # Flatten data
    corpus = [user_input] + [item for sublist in training_data.values() for item in sublist]
    print(f"\nCorpus: {corpus}") 
    
    # Create TFIDF Vectorizer
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus)
    print(f"TFIDF Matrix Shape: {tfidf_matrix.shape}") 

    # Compare input
    cosine_sim = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1:]) 
    similarity_scores = cosine_sim.flatten()
    print(f"Cosine Similarity Scores: {similarity_scores}")

    max_index = similarity_scores.argmax()
    print(f"Max Index: {max_index}")  
    
    offset = 0
    for label, phrases in training_data.items():
        if max_index < offset + len(phrases):
            print(f"[DEBUG] Classified Intent: {label}")
            return label
        offset += len(phrases)

    print("Defaulting to 'statement' intent")
    return "statement"

def generate_statistical_response(intent):
    return random.choice(responses.get(intent, responses["statement"]))