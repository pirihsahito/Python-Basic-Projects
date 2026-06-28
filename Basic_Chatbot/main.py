def chatbot_response(user):
    if user == "hi" or user == "hello" or user == "hey":
        return "Hello!"
    elif user == "how are you?" or user == "how are you" or user == "what's up?" or user == "what's up" or user == "whats up?" or user == "whats up":
        return "I am good."
    elif user == "who are you?" or user == "who are you" or user == "who?" or user == "who":
        return "I am a basic Chatbot - created by Sahito Pirih"
    elif user == "what is your favorite programming language?" or user == "what is your favorite programming language":
        return "Python Programming Language"
    else:
        return "I am sorry, I am a simple rule-based assitant and don't understand yet!"

print("I am a simple chatbot, which responses only these pre-defined messages:")
print("1. Greetings(Hi, Hello, etc...)")
print("2. How are you? or How are you")
print("3. Who are you? or Who are you or Who? or Who")
print("4. What is your favorite Programming Language? or What is your favorite Programming Language")

while True:
    try:
        user = input("You: ").lower().strip()

        response = chatbot_response(user)
        print(f"Chatbot: {response}")

    except ValueError:
        print("Invalid input! Tye pre-defined messages only.")

    exit = input("To end the chat press 'q' and to continue press any key: ").lower().strip()
    if exit == 'q':
        print("Thank You for using Chatbot! Goodbye! Have a good day")
        break
