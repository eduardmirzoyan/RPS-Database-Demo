import sqlite3


class Database:
    def __init__(self) -> None:
        self.connection = sqlite3.connect("rps.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS rps (
            is_win INTEGER,
            player_choice INTEGER,
            cpu_choice INTEGER
            )
            """
        )

    def log_game(self, is_win, player_choice, cpu_choice) -> None:
        self.cursor.execute(
            f"INSERT INTO rps VALUES ({is_win}, {player_choice}, {cpu_choice})"
        )
        self.connection.commit()

    def get_match_history(self) -> str:
        self.cursor.execute("SELECT rowid, * FROM rps")

        all_data = self.cursor.fetchall()

        if len(all_data) == 0:
            return "No recorded games."

        formatted_text = ""
        for game_data in all_data:
            formatted_text += f"Game {game_data[0]}: "

            # Handle player choice
            if game_data[2] == 1:
                formatted_text += "ROCK"
            elif game_data[2] == 2:
                formatted_text += "PAPER"
            elif game_data[2] == 3:
                formatted_text += "SISSORS"

            formatted_text += " vs "

            # Handle cpu choice
            if game_data[3] == 1:
                formatted_text += "ROCK "
            elif game_data[3] == 2:
                formatted_text += "PAPER "
            elif game_data[3] == 3:
                formatted_text += "SISSORS "

            # Handle game result
            if game_data[1] == 1:
                formatted_text += "[Win]"
            elif game_data[1] == 2:
                formatted_text += "[Loss]"
            elif game_data[1] == 3:
                formatted_text += "[Tie]"

            formatted_text += "\n"

        return formatted_text

    def get_winrate(self) -> str:
        self.cursor.execute("SELECT * FROM rps")

        all_data = self.cursor.fetchall()
        data_size = len(all_data)

        if data_size == 0:
            return "No recorded games."

        win_count = 0.0
        tie_count = 0.0
        lose_count = 0.0

        rock_count = 0
        paper_count = 0
        sissor_count = 0

        for game_data in all_data:
            if game_data[0] == 1:
                win_count += 1
            elif game_data[0] == 2:
                lose_count += 1
            elif game_data[0] == 3:
                tie_count += 1

            if game_data[1] == 1:
                rock_count += 1
            elif game_data[1] == 2:
                paper_count += 1
            elif game_data[1] == 3:
                sissor_count += 1

        formatted_text = f"Win-rate: {win_count/data_size*100:.1f}%;\nWin-or-Tie-rate: {(win_count+tie_count)/data_size*100:.1f}%;\n"

        formatted_text += "Favorite Throw: "
        largest = max(rock_count, paper_count, sissor_count)
        if largest == rock_count:
            formatted_text += "ROCK"
        elif largest == paper_count:
            formatted_text += "PAPER"
        elif largest == sissor_count:
            formatted_text += "SISSORS"

        self.cursor.execute("SELECT * FROM rps WHERE is_win == 2 AND cpu_choice == 1")
        all_data = self.cursor.fetchall()
        losses_to_rock = len(all_data)

        self.cursor.execute("SELECT * FROM rps WHERE is_win == 2 AND cpu_choice == 2")
        all_data = self.cursor.fetchall()
        losses_to_paper = len(all_data)

        self.cursor.execute("SELECT * FROM rps WHERE is_win == 2 AND cpu_choice == 3")
        all_data = self.cursor.fetchall()
        losses_to_sissor = len(all_data)

        formatted_text += "\nLost most to: "
        largest = max(losses_to_rock, losses_to_paper, losses_to_sissor)
        if largest == losses_to_rock:
            formatted_text += "ROCK"
        elif largest == losses_to_paper:
            formatted_text += "PAPER"
        elif largest == losses_to_sissor:
            formatted_text += "SISSORS"

        return formatted_text

    def clear(self):
        # Clear all records
        self.cursor.execute("DELETE FROM rps")

    def close(self) -> None:
        self.connection.commit()
        self.connection.close()
