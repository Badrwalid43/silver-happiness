print("Please think of a number between 0 and 100!")

low = 0
high = 100
state = True
while state:
    medium = (low + high) // 2
    print("Is your secret number " + str(medium) + "?")
    guess = input("Enter 'h' if the guess is too high, 'l' if too low, or 'c' if correct: ")
    if guess == "c":
        print("Game over. Your secret number was: " + str(medium))
        state = False
    elif guess == "h":
        high = medium
    elif guess == "l":
        low = medium
    else:
        print("Sorry, I did not understand your input.")
