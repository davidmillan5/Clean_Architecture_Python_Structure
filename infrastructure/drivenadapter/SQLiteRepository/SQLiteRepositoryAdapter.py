import sqlite3
from domain.model import User

class DatabaseAdapter:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.create_user_table()

    def create_user_table(self):
        with self.connection:
            self.connection.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL,
                    password TEXT NOT NULL
                )
            ''')

    def insert_user(self, user):
        with self.connection:
            self.connection.execute('''
                INSERT INTO users (id, name, email, password)
                VALUES (?, ?, ?, ?)
            ''', (user.id, user.name, user.email, user.password))

    def get_user_by_id(self, user_id):
        user_row = self.connection.execute('''
            SELECT id, name, email, password FROM users WHERE id = ?
        ''', (user_id,)).fetchone()

        if user_row:
            return User(*user_row)
        return None

    def close(self):
        self.connection.close()
