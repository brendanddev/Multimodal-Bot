
from utils.process_text import clean_utterance
from utils.pattern_matching import heuristic_match
from utils.speech_act import classify_speech_act
import regex as re


def understand(utterance, intents, regex_patterns):
    cleaned_utterance = clean_utterance(utterance)
    speech_act = classify_speech_act(utterance)
    print(f"Detected speech act: {speech_act}") # DEBUG
    intent = heuristic_match(cleaned_utterance, intents, regex_patterns)
    return intent 

def generate(intent, responses):
    if intent == -1:
        return "Sorry, I don't know the answer to that!"
    return responses[intent]
