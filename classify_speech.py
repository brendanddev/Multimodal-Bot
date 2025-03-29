"""
Linguistic Pattern Matching (Rule Based Linguistic Matching)
Brendan Dileo
"""

import spacy
from spacy.matcher import Matcher

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
