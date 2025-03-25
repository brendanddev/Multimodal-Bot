
import regex as re
from fuzzywuzzy import fuzz


def clean_utterance(utterance):
    clean = re.sub(r'[^\w\s]', '', utterance)
    clean = re.sub(r'\s+', ' ', clean).strip()
    print(f"Cleaned Utterance: '{clean}'")  # Debug print to check cleaned input
    return clean.lower()

def fuzzy_match(utterance, intents):
    best_match = None 
    best_score = -1

    for intent in intents:
        score = fuzz.ratio(utterance, intent)
        if score > best_score:
            best_score = score
            best_match = intent 

    return best_match, best_score

def understand(utterance, intents, regex_patterns):
    cleaned_utterance = clean_utterance(utterance)
    for i, pattern in enumerate(regex_patterns):
        if re.match(pattern, cleaned_utterance):
            return i
        
    match, score = fuzzy_match(cleaned_utterance, intents)
    if match and score > 65:
        return intents.index(match)
    
    return -1
