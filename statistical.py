
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import random

responses = {
    "greeting": ["Hello!", "Hi there!", "Hey! How's it going?"],
    "goodbye": ["Goodbye!", "See you later!", "Take care!"],
    "thank": ["You're welcome!", "No problem!", "Glad to help!"],
    "apology": ["No worries!", "It's okay!", "I understand."],
    "question": ["Hmm, let me think about that...", "That's a great question!", "Let me find out!"],
    "command": ["Okay, Ill try to do that!", "Got it, processing...", "Ill work on it."],
    "statement": ["Interesting! Tell me more.", "Oh, really?", "That makes sense."]
}

# Trarining data ishhh for classifying intent
training_data = {
    "greeting": ["hello", "hi", "hey", "greetings", "morning", "good evening"],
    "goodbye": ["bye", "goodbye", "see you", "farewell", "take care"],
    "thank": ["thanks", "thank you", "appreciate it"],
    "apology": ["sorry", "apologize", "myn bad", "pardon me"],
    "question": ["what", "how", "when", "where", "why", "is", "do", "can", "could", "would"],
    "command": ["give", "show", "tell", "bring", "help", "give me", "do"],
    "statement": ["I am", "it's", "this is", "they are", "there is", "was", "will be"]
}

def classify_statistical_intent(user_input):
    vectorizer = CountVectorizer().fit_transform([user_input] + [item for sublist in training_data.values() for item in sublist])
    cosine_sim = cosine_similarity(vectorizer[1:], vectorizer[0:1])
    similarity_scores = cosine_sim.flatten()
    max_index = similarity_scores.argmax()

    for label, phrases in training_data.items():
        if phrases:
            if max_index < len(phrases):
                return label
            max_index -= len(phrases)

    return "statement" 

def generate_statistical_response(intent):
    return random.choice(responses.get(intent, responses["statement"]))

def chatbot():
    print("Brendan's Statistical Test Bot! (Type 'exit' to quit)")

    while True:
        user_input = input(">>> ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        
        intent = classify_statistical_intent(user_input)
        response = generate_statistical_response(intent)
        print(f"Response: {response}\n")

if __name__ == "__main__":
    chatbot()
