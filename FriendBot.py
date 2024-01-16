import random

# List of possible user inputs
user_inputs = [
    "Hi",
    "How are you?",
    "What's your name?",
    "Tell me a joke",
    "What's the weather like today?",
    "What's your favorite color?",
    "Goodbye"
]

# List of possible bot responses
bot_responses = [
    "Hello!",
    "I'm good, thanks for asking.",
    "My name is ChatBot.",
    "Why don't scientists trust atoms? Because they make up everything!",
    "It's sunny today.",
    "My favorite color is blue.",
    "Goodbye!"
]

# Function to generate a random response from the bot
def generate_response(user_input):
    return random.choice(bot_responses)

# Main loop for the chatbot
while True:
    # Get user input
    user_input = input("User: ")

    # Check if user wants to exit
    if user_input.lower() == "goodbye":
        print("Bot: Goodbye!")
        break

    # Generate and print bot response
    bot_response = generate_response(user_input)
    print("Bot:", bot_response)
    