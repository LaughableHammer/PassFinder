import sqlite3
import hashlib

#Used https://www.youtube.com/watch?v=3NEzo3CfbPg for inspiration

class AccountManager:
    def __init__(self):
        self.conn = sqlite3.connect("TextFiles/userlogindata.db")
        self.cur = self.conn.cursor()

        # Create database if it doesn't already exist
        self.cur.execute("""     
            CREATE TABLE IF NOT EXISTS userlogindata (
                id INTEGER PRIMARY KEY,
                username VARCHAR(255) NOT NULL,
                password VARCHAR(255) NOT NULL
            )
        """)
        self.conn.commit()

    def create_account(self): #Get username, password and hash
        username = input("Enter username: ")
        password = input("Enter password: ")
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        #Store hashed password in database
        self.cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username, hashed_password))
        self.conn.commit()

        print("Account created successfully.")

    def login(self): #Get username, password and then hash
        username = input("Enter username: ")
        password = input("Enter password: ")
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        #Get the user details from database
        self.cur.execute("SELECT * FROM userdata WHERE username = ? AND password = ?", (username, hashed_password))
        user = self.cur.fetchone()
        #If user details exist and if they don't
        if user:
            print("Login successful.")
            #Add additional functionality here
        else:
            print("Invalid username or password.")


if __name__ == '__main__':
    account_manager = AccountManager()

    while True:
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            account_manager.create_account()
        elif choice == "2":
            account_manager.login()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")
