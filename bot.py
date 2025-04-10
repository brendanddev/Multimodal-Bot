
from data.load_data import load_json_data, load_regex_patterns
from intent import understand, generate

intents, responses = load_json_data() 
regex_patterns = load_regex_patterns()

def main():
    print("Welcome to Brendan's FAQ Bot!")
    print()
    print("To begin interacting with the bot, greet it.")
    print("For example, you can say 'hi', 'hello', or similar greetings!")
    print("To stop interacting with the bot, say goodbye.")
    print("For example, you can say 'goodbye', 'bye', or similar goodbyes!")

    while True:
        utterance = input(">>>").lower()
        intent = understand(utterance, intents, regex_patterns) 
        response = generate(intent, responses)
        print(response)
        print()


if __name__ == "__main__":
    main()