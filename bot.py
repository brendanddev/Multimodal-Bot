

def load_data():
    return None 

def understand(utterance):
    return None 

def generate(intent):
    return None

def main():
    print("Hello! I know stuff about chat bots. When you're done talking, just say 'goodbye'.")
    print()
    utterance = ""
    while True:
        utterance = input(">>> ")
        if utterance == "goodbye":
            break;
        intent = understand(utterance)
        response = generate(intent)
        print(response)
        print()

    print("Nice talking to you!")


if __name__ == "__main__":
    main()