
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