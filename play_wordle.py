import wordle
while True:
    choice = ""
    while choice != "1" and choice != "2":
        print("Enter 1 or 2")
        choice = input("1. Play\n2. Quit\n")
    if choice == "1":
        wordle.play_game()
    else:
        exit(0)
