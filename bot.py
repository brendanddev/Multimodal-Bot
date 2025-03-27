

from data.load_data import load_json_data, load_regex_patterns
from intent import understand

from classify_speech import classify_speech_act, analyze_sentiment, extract_entities
from statistical import classify_statistical_intent, generate_statistical_response



def generate(intent):
    if intent == -1:
        return "Sorry, I don't know the answer to that!"
    return responses[intent]

regex_patterns = load_regex_patterns()
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

        speech_act = classify_speech_act(utterance)  
        sentiment = analyze_sentiment(utterance)  
        entities = extract_entities(utterance)
        stats = classify_statistical_intent(utterance)
        stats_response = generate_statistical_response(utterance)

        intent = understand(utterance, intents, regex_patterns)
        response = generate(intent)

        print(f"Detected Speech Act: {speech_act}")
        print(f"Sentiment: {sentiment}")
        print(f"Extracted Entities: {entities}")
        print(f"Response: {response}\n")
    
        print(f"Statistical Response: {stats_response}\n")


        print(response)
        print()


if __name__ == "__main__":
    main()