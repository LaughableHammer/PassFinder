import sqlite3
import encryption
import decryption

class StorePassword:
    def __init__(self):
        self.conn = sqlite3.connect("TextFiles/Passwords.db")  # Connects to DB
        print("Opened DB successfully")
        self.cur = self.conn.cursor()

        # Create database if it doesn't already exist
        self.cur.execute(
            """     
            CREATE TABLE IF NOT EXISTS Passwords (
                id int NOT NULL,
                app_name VARCHAR(255) NOT NULL,
                stored_password VARCHAR(255),
                PRIMARY KEY (id)
            )
        """
        )
        self.conn.commit()
    
    def select_all_tasks(self): # for debugging from-> https://www.sqlitetutorial.net/sqlite-python/sqlite-python-select/
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


    def save_password(self, id: int, app_name: str, password: str) -> None:
        stored_password = str(password)#encryption.Encrypt(9, password) #encrypt password
        
        self.cur.execute(
            "INSERT INTO Passwords (id, app_name, stored_password) VALUES (?, ?, ?)",
            (int(id), str(app_name), str(stored_password)),
        )
        self.conn.commit()
        self.conn.close()
    
    def get_password(self, id: int, app_name: str) -> str:
        self.cur.execute(
            "SELECT stored_password FROM Passwords WHERE id = ? AND app_name = ?",
            (id, app_name),
        )
        password = self.cur.fetchone()

        if password:
            return decryption.Decrypt(9, password)  # decrypt
        else:
            return ""
        
if __name__ == "__main__":
    StorePassword = StorePassword()
    StorePassword.select_all_tasks()
    #StorePassword.save_password(8, 'Microsoft', '.windows43')