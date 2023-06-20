from dataclasses import dataclass
import sqlite3
import hashlib

# Used https://www.youtube.com/watch?v=3NEzo3CfbPg for inspiration


@dataclass
class User:
    user_id: int
    username: str
    password: str


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

        self.user: User | None = None

    def create_account(
        self,
        username: str,
        password: str,
    ) -> bool:
        """Allows the creation of accounts

        Args:
            username (str): takes in the user input for username
            password (str): takes in the user input for password

        Returns:
            bool: shows whether account was created or not
        """
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        # Check if username already exists in the database
        self.cur.execute(
            "SELECT COUNT(*) FROM userlogindata WHERE username = ? OR password = ?",  # SQL statement checks whether the username and password already exist
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

    def login(
        self,
        username: str,
        password: str,
    ) -> bool:
        """allows logging in to accounts that have previously been created

        Args:
            username (str): takes in account username from user input
            password (str): takes in account password from user input

        Returns:
            bool: describes whether the user details are correct (logs them in)
        """
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        # Get the user details from database
        self.cur.execute(
            "SELECT * FROM userlogindata WHERE username = ? AND password = ?",
            (username, hashed_password),
        )
        user = self.cur.fetchone()

        if user:
            user_id, username, password = user
            self.user = User(user_id, username, password)

        # If user details exist and if they don't
        return bool(user)

    def logout(
        self,
    ) -> bool:
        self.user = None
