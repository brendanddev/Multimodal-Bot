
import regex as re

def clean_utterance(utterance):
    """
    Cleans the input utterance by removing special characters, extra spaces, and 
    converting to lowercase.
    """
    clean = re.sub(r'[^\w\s]', '', utterance) 
    clean = re.sub(r'\s+', ' ', clean).strip()  
    print(f"Cleaned Utterance: '{clean}'")  
    return clean.lower()
