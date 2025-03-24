
import json 


def load_json_data():
    """
    Reads questions and answers, and returns two parallel key value lists.
    """
    try:
        with open("data/data.json", "r") as file:
            data = json.load(file) 
            print("Data Loaded Successfully!") 
        return data["questions"], data["answers"]
    except FileNotFoundError:
        print("Error: The data file is missing!")
    except json.JSONDecodeError: 
        print("Error: There was an issue decoding the JSON data!")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return [], []
