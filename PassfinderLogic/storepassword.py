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
        self,
    ):  # for debugging from-> https://www.sqlitetutorial.net/sqlite-python/sqlite-python-select/
        """
        Query all rows in the Passwords table
        :param conn: the Connection object
        :return:
        """
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM Passwords")

        rows = cur.fetchall()

        for row in rows:
            print(row)

    def save_password(self, username: str, app_name: str, password: str) -> None:
        encryptor = Encrypt(9)  # Create an instance of Encrypt with shift value 9 and plaintext password
        stored_password = encryptor.encrypt(password)  # Encrypt the password using the encrypt method

        self.cur.execute(
            "INSERT INTO Passwords (username, app_name, stored_password) VALUES (?, ?, ?)",
            (username, str(app_name), str(stored_password)),
        )
        self.conn.commit()

    def get_password(self, username: str, app_name: str) -> str:
        self.cur.execute(
            "SELECT stored_password FROM Passwords WHERE username = ? AND app_name = ?",
            (username, app_name),
        )
        password = self.cur.fetchone()

        if password:
            decryptor = Decrypt(9)  # Create an instance of Encrypt with shift value 9 and plaintext password
            return decryptor.decrypt(password)  # Encrypt the password using the encrypt method
        else:
            return ""

# if __name__ == "__main__":
#     StorePassword = StorePassword()
#     StorePassword.save_password('david', 'ok', 'so it workstwice in a row')
#     StorePassword.select_all_tasks()
#     print(StorePassword.get_password('david', 'ok'))
