def playback():
    user_input = input("What do you wanna say? ")
    slowed_input = user_input.replace(" ", "...")
    print(slowed_input)

def main():
    playback()

main()


