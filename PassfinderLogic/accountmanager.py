import sqlite3
import hashlib

# Used https://www.youtube.com/watch?v=3NEzo3CfbPg for inspiration


class AccountManager:
    def __init__(self):
        self.conn = sqlite3.connect("TextFiles/userlogindata.db")  # Connects to DB
        self.cur = self.conn.cursor()

        # Create database if it doesn't already exist
        self.cur.execute(
            """     
            CREATE TABLE IF NOT EXISTS userlogindata (
                id INTEGER PRIMARY KEY,
                username VARCHAR(255) NOT NULL,
                password VARCHAR(255) NOT NULL
            )
        """
        )
        self.conn.commit()

    # Creates an account for a new user
    # Each username and password combination must be unique
    # Username and password have already been input validated
    #
    # Parameter -> username - the username of the account being created
    # Parameter -> password - the password of the account being created
    #
    # Returns -> a boolean describing whether the account was created or not
    def create_account(
        self, username: str, password: str
    ) -> bool:  # Get username, password as a string
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        # Check if username already exists in the database
        self.cur.execute(
            "SELECT COUNT(*) FROM userlogindata WHERE username = ? AND password = ?",  # SQL statement checks whether the username and password already exist
            (username, hashed_password),
        )
        result = self.cur.fetchone()[0]  # fetches the results of the SQL query

        if result > 0:
            # Username or password already exists, return False
            return False

        self.cur.execute(
            "INSERT INTO userlogindata (username, password) VALUES (?, ?)",  # Store username and hashed password in database
            (username, hashed_password),
        )
        self.conn.commit()  # 'Saves' the changes

        return True

    # Allows the user to login to their account
    # Username and password have already been input validated
    #
    # Parameter -> username - the username of the account being logged into
    # Parameter -> password - the password of the account being logged into
    #
    # Returns -> a boolean describing whether the user is exists or not

    def login(
        self, username: str, password: str
    ) -> bool:  # Get username, password and then hash
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        # Get the user details from database
        self.cur.execute(
            "SELECT * FROM userlogindata WHERE username = ? AND password = ?",
            (username, hashed_password),
        )
        user = self.cur.fetchone()
        # If user details exist and if they don't

        return bool(user)

# if __name__ == '__main__':  used for debugging
#     account_manager = AccountManager()

#     while True:
#         print("1. Create Account")
#         print("2. Login")
#         print("3. Exit")

#         choice = input("Enter your choice: ")

#         if choice == "1":
#             account_manager.create_account()
#         elif choice == "2":
#             account_manager.login()
#         elif choice == "3":
#             break
#         else:
#             print("Invalid choice. Please try again.")
