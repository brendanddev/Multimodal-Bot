
import spacy
from spacy.matcher import Matcher
from textblob import TextBlob
import random

nlp = spacy.load("en_core_web_md")
matcher = Matcher(nlp.vocab)

speech_act_patterns = {
    "GREETING": [[{"LOWER": {"IN": ["hello", "hi", "hey", "greetings"]}}]],
    "GOODBYE": [[{"LOWER": {"IN": ["bye", "goodbye", "see you", "farewell"]}}]],
    "THANKING": [[{"LOWER": {"IN": ["thanks", "thank", "appreciate"]}}]],
    "APOLOGY": [[{"LOWER": {"IN": ["sorry", "apologize", "pardon"]}}]],
    "QUESTION": [[{"LOWER": {"IN": ["what", "where", "why", "how", "is", "when", "do"]}}]],
    "COMMAND": [[{"POS": "VERB", "LEMMA": {"IN": ["give", "get", "show", "tell"]}}]],
    "REQUEST": [
        [{"LOWER": {"IN": ["can", "could", "would", "please"]}}, {"POS": "VERB"}]
    ],
    "ASSERTION": [[{"POS": "PRON"}, {"POS": "VERB"}]],  # "I think", "She believes"
}

for label, pattern in speech_act_patterns.items():
    matcher.add(label, pattern)

def classify_speech_act(utterance):
    doc = nlp(utterance)
    matches = matcher(doc)
    
    for match_id, _, _ in matches:
        label = nlp.vocab.strings[match_id]
        return label.lower()
    
    return "statement" 

def analyze_sentiment(utterance):
    polarity = TextBlob(utterance).sentiment.polarity
    if polarity > 0.2:
        return "positive"
    elif polarity < -0.2:
        return "negative"
    return "neutral"

conversation_memory = {
    "last_intent": None,
    "topic": None,
    "user_name": None
}

def remember_context(utterance, intent):
    if intent in ["greeting"]:
        conversation_memory["last_intent"] = "greeting"
    elif intent in ["question", "command", "request"]:
        conversation_memory["topic"] = utterance  # Store topic
    elif intent in ["goodbye"]:
        conversation_memory["last_intent"] = "goodbye"

def generate_response(intent, sentiment, utterance):    
    responses = {
        "greeting": ["Hello!", "Hi there!", "Hey! Hows it going?"],
        "goodbye": ["Goodbye!", "See you later!", "Take care!"],
        "thanking": ["You're welcome!", "No problem!", "Glad to help!"],
        "apology": ["No worries!", "Its okay!", "I understand."],
        "question": ["Hmm, let me think about that...", "That's a great question!", "Let me find out!"],
        "command": ["Okay, Ill try to do that!", "Got it, processing...", "I'll work on it."],
        "request": ["Ill see what I can do.", "Let me check...", "I'll do my best!"],
        "positive": ["That's awesome!", "Great to hear that!", "That sounds amazing!"],
        "negative": ["I'm sorry to hear that. Is there anything I can do to help?", "That sounds tough.", "I understand, let me know how I can help."],
        "statement": ["Interesting! Tell me more.", "Oh, really?", "That makes sense."]
    }

    if intent in responses:
        return random.choice(responses[intent])
    
    if sentiment in responses:
        return random.choice(responses[sentiment])

    return "I'm here to chat!"

def chatbot():
    """Runs an interactive chatbot session."""
    print("Welcome to the Smart Chatbot! (Type 'exit' to quit)")

    while True:
        user_input = input(">>> ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        
        intent = classify_speech_act(user_input)
        sentiment = analyze_sentiment(user_input)
        remember_context(user_input, intent)

        response = generate_response(intent, sentiment, user_input)
        print(response)

if __name__ == "__main__":
    chatbot()
