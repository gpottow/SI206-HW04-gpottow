import random

questions = ["It is certain", "It is decidedly so", "Without a doubt",
            "Yes definitely", "You may rely on it", "As I see it, yes",
            "Most likely", "Outlook good", "Yes", "Signs point to yes",
            "Reply hazy try again", "Ask again later", "Better not tell you now",
            "Cannot predict now", "Concentrate and ask again", "Don't count on it",
            "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"]

def answer():
    return questions[random.randint(0,19)]


run = True
while run:
    user_input = input("What's your question?")
    if user_input.upper() == "QUIT":
        run = False
    elif not user_input.endswith('?'):
        print("I’m sorry, I can only answer questions.")
