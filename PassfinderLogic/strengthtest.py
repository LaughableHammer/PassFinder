import re  # provide regex capabilities


class PasswordStrengthTest:  # provide a rating for an inputted password
    def __init__(
        self,
    ):
        self.score = 20  # init score to 20, will be subtracted later if password is in common password list
        self.password_match = False
        self.common_passwords = []

    def load_common_passwords(
        self,
        filename,
    ):  # loads the common password file - https://www.w3schools.com/python/python_file_open.asp
        try:
            with open(filename, "r") as file:
                self.common_passwords = file.read().splitlines()
        except Exception as e:
            print("Error loading common passwords:", str(e))

    def calculate_score(
        self,
        password,
    ):
        length_password = len(password)

        if (
            0 < length_password < 5
        ):  # equivalent of casewhere which allocated points based on password length
            self.score += 10
        elif 4 < length_password < 8:
            self.score += 25
        elif 7 < length_password < 10:
            self.score += 40
        elif length_password > 9:
            self.score += 50

        # Used https://www.geeksforgeeks.org/password-validation-in-python/ for regex help

        if re.search(r"\d", password):  # uses REGEX to loop for numbers
            self.score += 10

        if re.search(r"\W", password):  # finds symbols and special characters
            self.score += 10

        if re.search(r"[a-z]", password):  # finds lowercase letters
            self.score += 5

        if re.search(r"[A-Z]", password):  # finds uppercase letters
            self.score += 5

    def check_common_password(
        self,
        password,
        filename,
    ):  # checks if password exists in common passwords file
        try:
            with open(filename, "r") as file:
                self.common_passwords = file.read().splitlines()
        except Exception as e:
            print("Error loading common passwords:", str(e))

        if password in self.common_passwords:
            self.password_match = True
            self.score -= 20

    def run_strength_test(
        self,
        password,
    ):
        filename = "TextFiles/SeclistsTop1000000"
        #self.load_common_passwords(filename)

        self.calculate_score(password)
        self.check_common_password(password, filename)

        result_message = f"Your password has a security rating of {self.score}%."

        if self.score < 100:
            result_message += "\nPlease read our password requirement guide to create a more secure password."

        return str(result_message)
    
strength_tester = PasswordStrengthTest()