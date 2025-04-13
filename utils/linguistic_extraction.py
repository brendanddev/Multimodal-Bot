"""
linguistic_extraction.py

Brendan Dileo, April 2025
"""

import spacy 
nlp = spacy.load("en_core_web_md")
string = "I hear GitLab is great for aliens working on a project!"

def extract_linguistics(utterance):
    """ Analyzes and prints the linguistic data from the users utterance """
    # Process the users utterance
    doc = nlp(utterance)

    # Tokens and Parts of speech
    print(" --- Tokens and POS --- ")
    for token in doc:
        print(f"{token.text:<15} POS: {token.pos_}")


if __name__ == "__main__":
    user_input = input("Please enter a sentence for linguistic analysis: ")
    extract_linguistics(user_input)