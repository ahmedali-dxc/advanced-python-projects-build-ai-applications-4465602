# Importing TextBlob to help the chatbot understand language nuances.
from textblob import TextBlob

# Define intents and their corresponding responses keyword matching
intents = {
    "hours": {
        "keywords": ["hours", "open", "close"],
        "response": "We are open from 9 AM to 5 PM, Monday to Friday."
    },
    "return": {
        "keywords": ["refund", "money back", "return"],
        "response": "I'd be happy to help you with the refund process. Let me transfer you to a live agent."
    }
}

# Defining the ChatBot class for interaction.
def get_response(message):
    # Convert the message to lowercase for consistent keywork matching 
    message = message.lower()

    # Check if the message contains any keywords associated with defined intents
    for intent_data in intents.values():
        if any(word in message for word in intent_data["keywords"]):
            # Reruring the coreesponding response if a keyword matches
            return intent_data["response"]
    
    # Analyzing the sentiment of the user's message.
    sentiment = TextBlob(message).sentiment.polarity

    # Return a response based on the sentiment score
    return (
        "That's so great to hear!" if sentiment > 0 else
        "I'm so sorry to hear that. How can I help?" if sentiment < 0 else
        "I see. Can you tell me more about that."
    )

def chat():
    # Greet the user and prompt for input
    print("Chatbot: Hi, how can I help you today?")
    # Continuously prompt the user for input until they choose to exit
    while(user_message := input("You: ").strip().lower()) not in ["exit", "quit", "bye"]:
        print(f"\nChatbot: {get_response(user_message)}")            

    # Thank the user for chatting when they exit
    print("Chatbot: Thank you for chatting. Have a great day!")
          


if __name__ == "__main__":
    # Start the chat when the script is executed
    chat()
