import os
import rps
import database


def main():
    db = database.Database()

    while True:
        os.system("cls")
        print("::: Welcome to RPS :::")
        print("~~~ What do you want to do? ~~~")
        print("1. Play Rock-Paper-Sissors")
        print("2. View statistics")
        print("3. Quit")
        value = input("-> ")

        if value == "1":
            play_rps(db)
        if value == "2":
            display_stats(db)
        if value == "3":
            break

    db.close()
    return 0


def play_rps(db: database.Database):
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
            result = game.play(choice)
            db.log_game(result[0], result[1], result[2])

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


def display_stats(db: database.Database):
    print("::: Displaying stats :::")
    statistics = db.get_stats()
    print(statistics)

    input("-> Press [ENTER] to go back...")


if __name__ == "__main__":
    main()
