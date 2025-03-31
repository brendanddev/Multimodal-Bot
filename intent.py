from utils.process_text import clean_utterance
import regex as re


def understand(utterance, intents, regex_patterns):
    cleaned_utterance = clean_utterance(utterance)
    for i, pattern in enumerate(regex_patterns):
        if re.match(pattern, cleaned_utterance):
            return i
    return -1
    


def generate(intent, responses):
    if intent == -1:
        return "Sorry, I don't know the answer to that!"
    return responses[intent]