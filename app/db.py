import sqlite3

class db:
    def connect(database):
        return sqlite3.connect(database)