from art import treasure_chest


# MAIN
print(treasure_chest)

game_is_in_progress = True

while game_is_in_progress:
    print("Welcome to Treasure Island.")
    print("Your mission is to find the treasure.")

    usr_input = input("Left or right? ").lower()

    if usr_input == "left":
        usr_input = input("Swim or wait? ").lower()

        if usr_input == "wait":
            usr_input = input("Red, yellow, or blue? ").lower()

            if usr_input == "yellow":
                print("You win!")
            elif usr_input == "red":
                print("You are burned by fire. Game over.")
            elif usr_input == "blue":
                print("You are eaten by beasts. Game over.")
            else:
                print("Game over")

        else:
            print("You are attacked by jellyfish. Game over.")

    else:
        print("You fall into a hole. Game over.")

    usr_input = input("Play again? (y/n) ").lower()

    if usr_input != "y":
        print("Goodbye")
        game_is_in_progress = False
