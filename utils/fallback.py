
"""
fallback.py

Brendan Dileo
"""

import spacy 
import random
from data.load_data import load_fallback_data
from utils.speech_act import classify_speech_act

nlp = spacy.load("en_core_web_md")
fallbacks, question_fallbacks, command_fallbacks, statement_fallbacks = load_fallback_data()

terms = {}
def fallback_response(utterance):
    doc = nlp(utterance)

    for token in doc:
        if token.lemma_.lower() in terms:
            return random.choice(fallbacks)
    
    # Check for entities
    for ent in doc.ents:
        if ent.label_ == "ORG":
            return f"I dont work for {ent.text}!"
        elif ent.label_ == "GPE":
            return f"Sorry, I've never been to {ent.text}!"
        elif ent.label_ == "LOCATION":
            return f"{ent.text} sounds like a great place! I have never been!"
        elif ent.label_ == "MONEY":
            return f"I don't know about {ent.text}, I wish I understood currency."
        elif ent.label_ == "DATE":
            return f"I'm not sure about {ent.text}, did you mean an in-game event?"
        elif ent.label_ == "TIME":
            return f"Time? Im not a clock!"
        elif ent.label_ == "PERSON":
            return f"Ah, {ent.text} sounds important.."
        elif ent.label_ == "EVENT":
            return f"Well I was not aware of {ent.text}, but Ill take note!"
        elif ent.label_ == "PRODUCT":
            return f"I dont have any details about {ent.text}."
        elif ent.label_ == "LANGUAGE":
            return f"I dont know how to speak {ent.text}, keyboard! Im happy to learn!"
        elif ent.label_ == "FAC":
            return f"{ent.text} sounds cool!"

    for chunk in doc.noun_chunks:
        if chunk.root.pos_ not in ['PRON', 'DET']:
            return f"Sorry, I dont know anything about {chunk.text}, but Im happy to learn about it!"
    
    # Check for common words
    for token in doc:
        if token.is_alpha and not token.is_stop:
            if token.is_alpha and not token.is_stop:
                if token.pos_ == "VERB":
                    return f"Sorry, I don't know how to {token.lemma_}, could you try rephrasing?"
                elif token.pos_ == "NOUN" and token.lemma_.lower() not in terms:
                    return f"I don't know anything about {token.text}, sorry!"
                elif token.pos_ == "ADJ":
                    return f"I do not know anything about {token.text}! Try to clarify."
                elif token.pos_ == "ADV":
                    return f"Sorry, I don't know what you mean by {token.text}!"
    
    speech_act = classify_speech_act(utterance)
    if speech_act == "question":
        return random.choice(question_fallbacks)
    elif speech_act == "command":
        return random.choice(command_fallbacks)
    elif speech_act == "statement":
        return random.choice(statement_fallbacks)
    return random.choice(fallbacks)

    