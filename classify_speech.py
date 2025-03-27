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
    "ASSERTION": [[{"POS": "PRON"}, {"POS": "VERB"}]], 
}

for label, pattern in speech_act_patterns.items():
    matcher.add(label, pattern)

location_patterns = [
    [
        {"LEMMA": "go"},
        {"LOWER": {"IN": ["to", "into", "toward"]}},
        {"POS": "DET"},
        {"POS": {"IN": ["ADJ", "PUNCT"]}, "OP": "*"},
        {"POS": "NOUN"}
    ]
]

matcher.add("LOCATION", location_patterns)

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

def extract_entities(utterance):
    doc = nlp(utterance)
    location_entities = []
    
    for ent in doc.ents:
        if ent.label_ == "GPE": 
            location_entities.append(ent.text)
    
    return location_entities

conversation_memory = {
    "last_intent": None,
    "topic": None,
    "user_name": None
}

def remember_context(utterance, intent):
    if intent in ["greeting"]:
        conversation_memory["last_intent"] = "greeting"
    elif intent in ["question", "command", "request"]:
        conversation_memory["topic"] = utterance 
    elif intent in ["goodbye"]:
        conversation_memory["last_intent"] = "goodbye"

def generate_response(intent, sentiment, utterance):    
    responses = {
        "greeting": ["Hello!", "Hi there!", "Hey! How's it going?"],
        "goodbye": ["Goodbye!", "See you later!", "Take care!"],
        "thanking": ["You're welcome!", "No problem!", "Glad to help!"],
        "apology": ["No worries!", "It's okay!", "I understand."],
        "question": ["Hmm, let me think about that...", "That's a great question!", "Let me find out!"],
        "command": ["Okay, I'll try to do that!", "Got it, processing...", "I'll work on it."],
        "request": ["I'll see what I can do.", "Let me check...", "I'll do my best!"],
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
    print("Brendan's Testing Bot! (Type 'exit' to quit)")

    while True:
        user_input = input(">>> ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        
        intent = classify_speech_act(user_input)
        sentiment = analyze_sentiment(user_input)
        remember_context(user_input, intent)
        
        location_entities = extract_entities(user_input)
        
        # Debugging (TODO: REMOVE ME)
        print("\n--- Debugging Information ---")
        print(f"User Input: {user_input}")
        print(f"Detected Intent: {intent}")
        print(f"Sentiment: {sentiment}")
        if location_entities:
            print(f"Location Entities: {', '.join(location_entities)}")
        else:
            print("No location entities detected.")
        
        response = generate_response(intent, sentiment, user_input)
        print(f"Response: {response}\n")

if __name__ == "__main__":
    chatbot()
