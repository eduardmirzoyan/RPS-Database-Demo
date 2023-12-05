import random

"""
Simulates a game of Rock-Paper-Sissors

1 - Rock
2 - Paper
3 - Sissors

Results
win/lose/tie : 1/2/3
player r/p/s = 1/2/3
cpu r/p/s = 1/2/3
"""

table = {1: "ROCK", 2: "PAPER", 3: "SISSORS"}


class RPS:
    def __init__(self) -> None:
        pass

    def play(self, choice: int) -> []:
        # Check for valid input
        if choice > 3 or choice < 1:
            raise Exception(f"UNHANDLED INPUT: {choice}")

        result = [0, 0, 0]

        result[1] = choice

        # Randomly choose
        cpu_choice = random.randint(1, 3)
        result[2] = cpu_choice

        print(f"You chose [{table[choice]}], CPU chose [{table[cpu_choice]}]")

        # Check for tie
        if cpu_choice == choice:
            result[0] = 3
            print("You Tie!")

        # Check for win
        elif choice == 1 and cpu_choice == 3:
            result[0] = 1
            print("You Win!")
        elif choice == 2 and cpu_choice == 1:
            result[0] = 1
            print("You Win!")
        elif choice == 3 and cpu_choice == 2:
            result[0] = 1
            print("You Win!")

        # Check for loss
        else:
            result[0] = 2
            print("You Lose!")

        return result
