


run = True
while run:
    user_input = input("What's your question?")
    if user_input.upper() == "QUIT":
        run = False
    elif not user_input.endswith('?'):
        print("I’m sorry, I can only answer questions.")
