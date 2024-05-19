import sqlite3
from pathlib import Path

class Database:
    def __init__(self, path: Path):
        self.connection = sqlite3.connect(path)
        self.cursor = self.connection.cursor()

        self.cursor.executescript((Path(__file__).parent.parent / "init.sql").read_text())
        self.connection.commit()