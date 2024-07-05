import random

def greetings():
    responses = ["Hello", "Hi there!", "Hey", "Nice to meet you", "Wassup nigga", "How can I help you?"]
    return random.choice(responses)

def farewell():
    responses = ["Byee!!","Have a good day","See you later","Goodbye!!"]
    return random.choice(responses)

def respond(message):
    if any(word in message.lower() for word in ["hello", "hi", "hey"]):
        return greetings()
    if any(word in message.lower() for word in ["bye", "see you", "tata"]):
        return farewell()
    elif "how are you?" in message.lower():
        return "I am a bot, I am doing well, thanks for asking :)"
    elif "what's your name?" in message.lower():
        return "I am Panda the chatbot! How can I assist you today?"
    else:
        return "Sorry I didn't catch that."

def main():
    print("Chatbot: " + greetings())
    while True:
        user_input = input("You: ")
        if any(word in user_input.lower() for word in ["bye", "see you", "tata"]):
            print("Chatbot: " + farewell())
            break
        else:
            print("Chatbot: " + respond(user_input))
        
