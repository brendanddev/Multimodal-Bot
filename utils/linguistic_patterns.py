"""
linguistic_patterns.py

Brendan Dileo, April 2025
"""

import spacy 
from spacy.matcher import Matcher

nlp = spacy.load("en_core_web_md")

def match_patterns(utterance):
    # Initialize matcher
    matcher = Matcher(nlp.vocab)

    pattern = [
        # Common question words
        {"LOWER": {"in": ["who", "what", "were", "where", "when", "why", "how"]}}, 
        # Token must be aux verb and occur one or more times
        {"POS": "AUX", "OP": "+"},
        # Token must be a pronoun but is optional
        {"POS": "PRON", "OP": "?"}  
    ]

    # Add the pattern to the matcher
    matcher.add("QUESTION_PATTERN", [pattern])

    # Process the users utterance into a doc object
    doc = nlp(utterance)

    # Find all the matches in the doc object
    matches = matcher(doc)

    if matches:
        print("\n--- Question Pattern Matches Found ---")
        for match_id, start, end in matches:
            pattern_id = nlp.vocab.strings[match_id]
            span = doc[start:end]  # The matched span
            print(f"Match ID: {pattern_id}, Matched phrase: {span.text}")
    else:
        print("\nNo question matches found.")

if __name__ == "__main__":
    user_input = input("Enter a sentence for question pattern matching: ")
    match_patterns(user_input)
