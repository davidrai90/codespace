# app.py
import datetime

def chatbot_response(user_input):

    # convert input to case-insensitive form
    user_input = user_input.casefold()

    
    if "hello" in user_input:
        return "Hi there! How can I help you?"
    elif "time" in user_input:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
    elif "joke" in user_input:
        return "I am a machine, I rechared my self when I feel tired!"
    elif "bye" in user_input:
        return "Goodbye! Have a nice day."
    elif "how are you" in user_input:
        return "I'm just a bot, but I'm doing great!"
    else:
        return "Sorry, I don't understand that yet."

print("Welcome to Simple Chatbot! (type 'exit' to quit)")

while True:
    user_input = input("You: ")
    if user_input.casefold() == "exit":
        print("Chatbot: Bye!")
        break
    response = chatbot_response(user_input)
    print("Chatbot:", response)
