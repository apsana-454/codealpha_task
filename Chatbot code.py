print("Chatbot: Hello! Type 'bye' to exit.")

def chatbot_response(user_input):
    text = user_input.strip().lower()

    if text == "hello":
        return "Hi!"
    elif text == "how are you":
        return "I'm fine, thanks!"
    elif text == "bye":
        return "Goodbye!"
    else:
        return "Sorry, I don't understand that."

while True:
    user_message = input("You: ")
    reply = chatbot_response(user_message)
    print("Chatbot:", reply)

    if user_message.strip().lower() == "bye":
        break
