"""
bot.py

Brendan Dileo, April 2025
"""

from multimodal_bot.data.load_data import load_json_data, load_regex_patterns
from multimodal_bot.core.intent import understand, generate

intents, responses = load_json_data() 
regex_patterns = load_regex_patterns()

def main():
    print("Welcome to Brendan's Multimodal Bot!")
    print()
    print("To begin interacting with the bot, greet it.")
    print("For example, you can say 'hi', 'hello', or similar greetings!")
    print("To stop interacting with the bot, say goodbye.")
    print("For example, you can say 'goodbye', 'bye', or similar goodbyes!")

    # basic control loop for terminal interactions
    while True:
        utterance = input(">>>")
        response, intent = understand(utterance, intents, regex_patterns)
        reply = generate(intent, response, responses, utterance)
        print(reply)
        print()

if __name__ == "__main__":
    main()