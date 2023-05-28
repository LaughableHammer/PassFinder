import sqlite3

from PassfinderLogic.encryption import Encrypt
from PassfinderLogic.decryption import Decrypt

class StorePassword:
    def __init__(self):
        self.conn = sqlite3.connect("TextFiles/passwords.db")  # Connects to DB
        self.cur = self.conn.cursor()

        # Create database if it doesn't already exist
        self.cur.execute(
            """     
            CREATE TABLE IF NOT EXISTS passwords (
                id INTEGER PRIMARY KEY,
                app_name VARCHAR(255) NOT NULL,
                stored_password VARCHAR(255) NOT NULL
            )
        """
        )
        self.conn.commit()
        
    def save_password(self, id: int, app_name: str, password: str) -> None:
        
        encrypted_password = Encrypt(9, password) #encrypt password
        
        self.cur.execute(
            "INSERT INTO passwords (id, app_name, encrypted_password) VALUES (?, ?, ?)",
            (id, app_name, encrypted_password),
        )
        self.conn.commit()

    def get_password(self, id: int, app_name: str) -> str:
        self.cur.execute(
            "SELECT encrypted_password FROM passwords WHERE id = ? AND app_name = ?",
            (id, app_name),
        )
        password = self.cur.fetchone()

        if password:
            return Decrypt(9, password)  # decrypt
        else:
            return ""