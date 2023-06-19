import random
import string


class PasswordGenerator:
    # def __init__(self):

    def generate_password(
        self,
        length: str,
        special_characters: bool,
        numbers: bool,
        normal_characters: bool,
    ):
        characters = ""

        if special_characters:
            characters += string.punctuation
        if numbers:
            characters += string.digits
        if normal_characters:
            characters += string.ascii_letters
        """if not characters:
            print("You need to select some characters!")
            self.password_options()
            self.generate_password()"""
        password = "".join(
            random.choice(characters) for i in range(int(length))
        )  # concatenate all the randomly generated characters from the valid characters
        return password
