
"""
speech_act.py

Brendan Dileo, April 2025
"""

import spacy 
from spacy.matcher import Matcher

nlp = spacy.load("en_core_web_md")
matcher = Matcher(nlp.vocab)

question_patterns = [
    [{"LOWER": {"IN": ["what", "where", "why", "how", "is", "when", "do"]}}]
]

command_patterns = [
    [{"POS": "VERB", "LEMMA": "give"}],  
    [{"POS": "VERB", "LEMMA": "get"}],
    [{"POS": "VERB", "LEMMA": "read"}],  
    [{"LOWER": "please"}, {"POS": "VERB"}]
]

matcher.add("QUESTION", question_patterns)
matcher.add("COMMAND", command_patterns)

def classify_speech_act(utterance):
    doc = nlp(utterance)
    matches = matcher(doc)

    # Check whether utterance is a question, statement, etc
    for match_id, start, end in matches:
        if nlp.vocab.strings[match_id] == "QUESTION":
            return "question"
        elif nlp.vocab.strings[match_id] == "COMMAND":
            return "command"
    return "statement"