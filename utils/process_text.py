
import regex as re

def clean_utterance(utterance):
    clean = re.sub(r'[^\w\s]', '', utterance) 
    clean = re.sub(r'\s+', ' ', clean).strip() 
    return clean.lower()
