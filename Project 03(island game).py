#photo game
print("""███████████████████████████
███████▀▀▀░░░░░░░▀▀▀███████
████▀░░░░░░░░░░░░░░░░░▀████
███│░░░░░░░░░░░░░░░░░░░│███
██▌│░░░░░░░░░░░░░░░░░░░│▐██
██░└┐░░░░░░░░░░░░░░░░░┌┘░██
██░░└┐░░░░░░░░░░░░░░░┌┘░░██
██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██
██▌░│██████▌░░░▐██████│░▐██
███░│▐███▀▀░░▄░░▀▀███▌│░███
██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██
██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██
████▄─┘██▌░░░░░░░▐██└─▄████
█████░░▐█─┬┬┬┬┬┬┬─█▌░░█████
████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████
█████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████
███████▄░░░░░░░░░░░▄███████
██████████▄▄▄▄▄▄▄██████████
███████████████████████████
""")
rom_red = input("""welcome to my island
there are you two doors in front of you. 🚪 a red door and 🚪 a blue door
wich door do you want open ? \n
""").lower()

if rom_red == "red":
    box_green = input("""great! now you entered a room. 
    you found three boxes: white 🎁 , black 🎁 , green 🎁
    wich box do you open ? \n """).lower()

    if box_green == "green":
        print('Congratulations! You found 💰💰💰 ')
    elif box_green == "white":
        print("""opss! game over
        it's 🐯 🐯 🐯""")
    elif box_green == "black":
        print("""opss!  game over
        🐜🐜🐜 """)
    else:
        print("pleas choose the box ")

elif rom_red == "blue":
    print("""opss! game over
    it's 🐯 🐯 🐯""")

else:
    print("invalid choice 👺👺👺 ")
