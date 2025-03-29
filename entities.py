
"""
Linguistic Processing with Named Entity Recognition and POS-based Analysis.
Brendan Dileo
"""

import spacy

nlp = spacy.load("en_core_web_md")

def extract_entities(utterance):
    doc = nlp(utterance)
    entity_responses = []

    for ent in doc.ents:
        if ent.label_ == "ORG":
            entity_responses.append(f"I do not work for {ent.text}!")
        elif ent.label_ == "GPE":
            entity_responses.append(f"Sorry, I've never been to {ent.text}!")
        elif ent.label_ == "LOCATION":
            entity_responses.append(f"{ent.text} sounds like a great place! I have never been!")
        elif ent.label_ == "MONEY":
            entity_responses.append(f"I'm not familiar with currencies like {ent.text}!")
        elif ent.label_ == "DATE":
            entity_responses.append(f"I'm not sure when {ent.text} is...")
        elif ent.label_ == "TIME":
            entity_responses.append(f"Time? I'm not a clock!")
        elif ent.label_ == "PERSON":
            entity_responses.append(f"Ah, {ent.text} sounds important!")
        elif ent.label_ == "EVENT":
            entity_responses.append(f"Well, I was not aware of {ent.text}, but I'll take note!")
        elif ent.label_ == "PRODUCT":
            entity_responses.append(f"I don't have any details about {ent.text}!")
        elif ent.label_ == "LANGUAGE":
            entity_responses.append(f"I don't know how to speak {ent.text}!")
        elif ent.label_ == "FAC":
            entity_responses.append(f"{ent.text} sounds cool!")

    for chunk in doc.noun_chunks:
        if chunk.root.pos_ not in ['PRON', 'DET']:
            entity_responses.append(f"Sorry, I don't know anything about {chunk.text}!")

    for token in doc:
        if token.is_alpha and not token.is_stop:
            if token.pos_ == "VERB":
                entity_responses.append(f"Sorry, I don't know how to {token.lemma_}, could you try rephrasing?")
            elif token.pos_ == "NOUN":
                entity_responses.append(f"I don't know anything about {token.text}, sorry!")
            elif token.pos_ == "ADJ":
                entity_responses.append(f"I do not know anything about {token.text}! Try to clarify.")
            elif token.pos_ == "ADV":
                entity_responses.append(f"Sorry, I don't know what you mean by {token.text}!")

    return entity_responses
