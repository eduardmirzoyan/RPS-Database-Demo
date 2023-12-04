import sqlite3


class Database:
    def __init__(self) -> None:
        self.connection = sqlite3.connect("rps.db")
        self.cursor = self.connection.cursor()

    def close(self) -> None:
        self.connection.commit()
        self.connection.close()
