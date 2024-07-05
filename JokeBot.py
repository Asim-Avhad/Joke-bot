import requests

def get_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)
    data = response.json()
    return f"Joke: {data['setup']}\nAnswer: {data['punchline']}"

def main():
    print("Chatbot: Hi! I'm JokeBot. Would you like to hear a joke?")
    while True:
        user_input = input("You: ")
        if any(word in user_input.lower() for word in ["bye", "see you", "tata"]):
            print("Chatbot: Goodbye!")
            break
        elif any(word in user_input.lower() for word in ["yes", "yeah", "sure", "okay", "please"]):
            print("Chatbot:", get_joke())
        else:
            print("Chatbot: Okay, let me know if you want to hear a joke.")

if __name__ == "__main__":
    main()