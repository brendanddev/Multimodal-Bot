# bot.py

from data.load_data import load_json_data
from intent import understand, generate
intents, responses = load_json_data() 

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
        intent = understand(utterance, intents)
        response = generate(intent, responses)
        print(response)
        print()


if __name__ == "__main__":
    main()