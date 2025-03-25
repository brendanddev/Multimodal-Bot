
from data.load_data import load_json_data, load_regex_patterns
from intent import understand

def generate(intent):
    if intent == -1:
        return "Sorry, I don't know the answer to that!"
    return responses[intent]

regex_patterns = load_regex_patterns()
print(regex_patterns)
intents, responses = load_json_data() 

def main():
    print("Welcome to Brendan's Bot!")
    print()
    print("To begin interacting with the bot, greet it.")
    print("For example, you can say 'hi', 'hello', or similar greetings!")
    print("To stop interacting with the bot, say goodbye.")
    print("For example, you can say 'goodbye', 'bye', or similar goodbyes!")

    while True:
        utterance = input(">>>").lower()

        intent = understand(utterance, intents, regex_patterns)
        response = generate(intent)
        print(response)
        print()


if __name__ == "__main__":
    main()