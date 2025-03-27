
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import random

def chatbot():
    print("Brendan's Statistical NLP Test Bot. (Type 'exit' to quit)")

    while True:
        user_input = input(">>> ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        
        intent = classify_intent(user_input)
        response = generate_response(intent)
        print(f"Response: {response}\n")

if __name__ == "__main__":
    chatbot()
