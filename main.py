import os
import rps


def main():
    while True:
        os.system("cls")
        print("::: Welcome to RPS :::")
        print("~~~ What do you want to do? ~~~")
        print("1. Play Rock-Paper-Sissors")
        print("2. View statistics")
        print("3. Quit")
        value = input("-> ")

        if value == "1":
            play_rps()
        if value == "2":
            display_stats()
        if value == "3":
            break

    return 0


def play_rps():
    game = rps.RPS()
    while True:
        os.system("cls")
        print("~~~ What will you throw? ~~~")
        print("1. Rock")
        print("2. Paper")
        print("3. Sissors")
        value = input("-> ")
        if value == "1" or value == "2" or value == "3":
            choice = int(value)

            os.system("cls")
            game.play(choice)

            print("\n~~~ Play again? ~~~")
            print("1. Yes")
            print("2. No")
            value = input("-> ")
            if value == "1":
                continue
            else:
                break
        else:
            print("Invalid input...")


def display_stats():
    print("::: Displaying stats :::")
    input("-> Press [ENTER] to go back...")


if __name__ == "__main__":
    main()
