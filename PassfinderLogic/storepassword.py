import sqlite3

from PassfinderLogic.encryption import Encrypt
from PassfinderLogic.decryption import Decrypt


class StorePassword:
    def __init__(self):
        self.conn = sqlite3.connect("TextFiles/Passwords.db")  # Connects to DB
        print("Opened DB successfully")
        self.cur = self.conn.cursor()

        # Create database if it doesn't already exist
        self.cur.execute(
            """     
            CREATE TABLE IF NOT EXISTS Passwords (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                username VARCHAR(255) NOT NULL,
                app_name VARCHAR(255) NOT NULL,
                stored_password VARCHAR(255)
            )
        """
        )
        self.conn.commit()

    def select_all_tasks(
        self,):  # for debugging from-> https://www.sqlitetutorial.net/sqlite-python/sqlite-python-select/
        #selects everything in the database, only used for debugging
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM Passwords")

        rows = cur.fetchall()

        for row in rows:
            print(row)

    def save_password(self, username: str, app_name: str, password: str) -> None:
        """saves a password for a user

        Args:
            username (str): the user username, this is stored in a file when the user logs in
            app_name (str): the name of the app of the password being stored
            password (str): the password of the app being stored

        Returns:
            bool: describes whether the password was successfully saved
        """
        encryptor = Encrypt(
            9
        )  # Create an instance of Encrypt with shift value 9 and plaintext password
        stored_password = encryptor.encrypt(
            password
        )  # Encrypt the password using the encrypt method

        self.cur.execute(
            "INSERT INTO Passwords (username, app_name, stored_password) VALUES (?, ?, ?)",
            (username, str(app_name), str(stored_password)),
        )
        save = self.cur.fetchone()
        self.conn.commit()

        return True

    def get_password(self, username: str) -> str:
        """uses the username to get all the passwords from the database

        Args:
            username (str): the username of the user, pre-stored in a file to prevent malicious behaviour

        Returns:
            results (str): all the app names and their respective passwords
        """
        self.cur.execute(
            "SELECT app_name, stored_password FROM Passwords WHERE username = ?",
            (username,),
        )
        passwords = self.cur.fetchall()

        decryptor = Decrypt(9)
        results = [
            (app_name, decryptor.decrypt(password)) for app_name, password in passwords
        ]
        return results