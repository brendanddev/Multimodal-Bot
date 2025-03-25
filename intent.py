import regex as re
from fuzzywuzzy import fuzz


def clean_utterance(utterance):
    clean = re.sub(r'[^\w\s]', '', utterance) 
    clean = re.sub(r'\s+', ' ', clean).strip()  
    print(f"Cleaned Utterance: '{clean}'")  
    return clean.lower()


def understand(utterance, intents, regex_patterns):
    cleaned_utterance = clean_utterance(utterance)
    print(f"Trying to match cleaned utterance: '{cleaned_utterance}'")  
    for i, pattern in enumerate(regex_patterns):
        print(f"Testing pattern: '{pattern}' against cleaned utterance: '{cleaned_utterance}'") 
        if re.match(pattern, cleaned_utterance, re.IGNORECASE):  
            print(f"Pattern matched! Returning index {i}")  
            return i
    
    print("No match found.") 
    return -1