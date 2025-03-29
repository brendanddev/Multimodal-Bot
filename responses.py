

import random

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

def generate_response(intent, sentiment):
    if intent in responses:
        return random.choice(responses[intent])
    
    if sentiment in responses:
        return random.choice(responses[sentiment])

    return "I'm here to chat!"
