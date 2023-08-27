from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a ChatBot instance
chatbot = ChatBot('MyBot')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot on English language data
trainer.train('chatterbot.corpus.english')


def main():
    print("ChatBot: Hello! How can I assist you today?")

    while True:
        user_input = input("You: ")

        if user_input.lower() == 'bye':
            print("ChatBot: Goodbye!")
            break

        response = chatbot.get_response(user_input)
        print("ChatBot:", response)


if __name__ == "__main__":
    main()
