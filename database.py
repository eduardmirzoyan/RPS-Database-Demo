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
        print("Added game to database.")

    def get_stats(self) -> str:
        self.cursor.execute("SELECT * FROM rps")

        data = self.cursor.fetchall()

        formatted_text = ""
        for game_data in data:
            # Handle game result
            if game_data[0] == 1:
                formatted_text += "Win, "
            elif game_data[0] == 2:
                formatted_text += "Lose, "
            elif game_data[0] == 3:
                formatted_text += "Tie, "

            # Handle player choice
            formatted_text += " Player: "
            if game_data[1] == 1:
                formatted_text += "Rock,"
            elif game_data[1] == 2:
                formatted_text += "Paper,"
            elif game_data[1] == 3:
                formatted_text += "Sissors,"

            # Handle cpu choice
            formatted_text += " CPU: "
            if game_data[2] == 1:
                formatted_text += "Rock"
            elif game_data[2] == 2:
                formatted_text += "Paper"
            elif game_data[2] == 3:
                formatted_text += "Sissors"

            formatted_text += "\n"

        return formatted_text

    def close(self) -> None:
        self.connection.commit()
        self.connection.close()
