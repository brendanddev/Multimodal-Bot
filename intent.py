

from text_processing import clean_utterance
from pattern_matching import heuristic_match

def understand(utterance, intents, regex_patterns):
    """
    Attempts to understand the users utterance by determining their intent.
    """
    cleaned_utterance = clean_utterance(utterance)

    match, score = heuristic_match(cleaned_utterance, intents, regex_patterns)
    if match != -1:
        return match
    return -1