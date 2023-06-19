import re  # provide regex capabilities

'''
    NOTE:
    Good use of reference comments. It is good to see that you
    are crediting other authors on their code and guidance. 
    
    You are not using docstrings. Please ensure that you are
    using these to give information about your functions and 
    classes. They will help you use them elsewhere in your code
    and also help the linter in picking types.
    
    Your code is littered with magic numbers. You should make 
    sure that you are parametrizing your code so that it is easily
    usable or maintainable. 
    
    The magic values extend to your password checker score.
    What if you want to use different methods on how to check
    passwords. 
    Instead of having a function for each you can have an object
    that conforms to a base class of password_checker. This will then 
    be passed to the PasswordStrengthChecker  class. Then the user 
    can compose their own set of tests, or you can easily add more 
    in the future. 
    
    You likewise should not be using print for your application. It is 
    GUI so everything should be shown on the GUI not the terminal.
'''


class PasswordStrengthTest:  # provide a rating for an inputted password
    def __init__(self):
        self.score = 20  # init score to 20, will be subtracted later if password is in common password list
        self.password_match = False
        self.common_passwords = []

    def load_common_passwords(
        self, filename
    ):  # loads the common password file - https://www.w3schools.com/python/python_file_open.asp
        try:
            with open(filename, "r") as file:
                self.common_passwords = file.read().splitlines()
        except Exception as e:
            print("Error loading common passwords:", str(e))

    def calculate_score(self, password):
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
        self, password
    ):  # checks if password exists in common passwords file
        if password in self.common_passwords:
            self.password_match = True
            self.score -= 20

    def run_strength_test(self):  # coordinates the strength test
        filename = "TextFiles/SeclistsTop1000000"
        self.load_common_passwords(filename)
        password_input = input("Enter your password: ")

        self.calculate_score(password_input)
        self.check_common_password(password_input)

        print(
            "Your password has a security rating of " + str(self.score) + "%."
        )  # displays results
        if self.score < 100:
            print(
                "Please read our password requirement guide to create a more secure password."
            )


if __name__ == "__main__":
    password_tester = PasswordStrengthTest()
    password_tester.run_strength_test()
