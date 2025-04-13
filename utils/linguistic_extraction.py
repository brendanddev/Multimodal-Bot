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
    
    # Noun Chunks
    print(" --- Noun Chunks --- ")
    for chunk in doc.noun_chunks:
        print(f"{chunk.text}")

    # Named Entitiy Recognition (NER)
    print("\n --- Entities --- ")
    for ent in doc.ents:
        print(ent.text, ent.label_)

    # Lemmatization and Lemmas
    print("\n --- Lemmas --- ")
    for token in doc:
        print(token.text, "->", token.lemma_)

    # Dependency Parsing
    print("\n --- Dependency Parsing --- ")
    for token in doc:
        print(f"{token.text} <--{token.dep_}-- {token.head.text}")


if __name__ == "__main__":
    user_input = input("Please enter a sentence for linguistic analysis: ")
    extract_linguistics(user_input)