import nltk
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how are you today?",]
    ],
    [
        r"what is your name?",
        ["My name is ChatBot and I'm here to assist you.",]
    ],
    [
        r"how are you?",
        ["I'm doing good, thank you!",]
    ],
    [
        r"(.*) sorry (.*)",
        ["It's alright, no problem.",]
    ],
    [
        r"quit",
        ["Bye, take care. See you soon!"]
    ],
]

# Create a chatbot instance
def chatbot():
    print("Hi! I'm ChatBot. How can I assist you today?")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    nltk.download('punkt')
    chatbot()
