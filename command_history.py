command_history = []

while True:
    user_input = input("What is your command? ")
    if user_input == "history":
        for commands in command_history:
            print(commands)
    elif user_input == "exit":
        break
    else:
        command_history.append(user_input)

