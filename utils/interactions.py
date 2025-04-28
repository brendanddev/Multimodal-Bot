
"""
greetings.py

Brendan Dileo, April 2025
"""


import random 
import spacy 

from spacy.matcher import Matcher, PhraseMatcher
from data.load_data import load_response_data

nlp = spacy.load("en_core_web_md")
intents = load_response_data()
matcher = PhraseMatcher(nlp.vocab, attr="LOWER")

for intent, data in intents.items():
    patterns = data["patterns"]
    matcher.add(intent, [nlp(text) for text in patterns])


def detect_response(utterance):
    doc = nlp(utterance)
    matches = matcher(doc)

    if matches:
        match_id, start, end = matches[0]
        intent = nlp.vocab.strings[match_id]
        response = random.choice(intents[intent]["responses"])
        return response 
    
    return None