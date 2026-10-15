def convert():
    user_emoticon = input("Happy or sad emoticon? ")
    user_update = user_emoticon.replace(":)", "🙂").replace(":(", "🙁")
    print(user_update)

def main():
    convert()

main()

