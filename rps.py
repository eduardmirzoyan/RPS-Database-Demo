import random

"""
Simulates a game of Rock-Paper-Sissors

1 - Rock
2 - Paper
3 - Sissors
"""

table = {1: "ROCK", 2: "PAPER", 3: "SISSORS"}


class RPS:
    def __init__(self) -> None:
        pass

    def play(self, choice: int) -> None:
        # Check for valid input
        if choice > 3 or choice < 1:
            raise Exception(f"UNHANDLED INPUT: {choice}")

        # Randomly choose
        cpu_choice = random.randint(1, 3)

        print(f"You chose [{table[choice]}], CPU chose [{table[cpu_choice]}]")

        # Check for tie
        if cpu_choice == choice:
            print("You Tie!")

        # Check for win
        elif choice == 1 and cpu_choice == 3:
            print("You Win!")
        elif choice == 2 and cpu_choice == 1:
            print("You Win!")
        elif choice == 3 and cpu_choice == 2:
            print("You Win!")

        # Check for loss
        else:
            print("You Lose!")
