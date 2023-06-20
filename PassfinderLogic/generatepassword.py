import random
import string


class PasswordGenerator:
    def generate_password(
        self,
        length: str,
        special_characters: bool,
        numbers: bool,
        normal_characters: bool,
    ):
        characters = ""

        if special_characters:
            characters += (
                string.punctuation
            )  # Add special characters to the character pool
        if numbers:
            characters += string.digits  # Add numbers to the character pool
        if normal_characters:
            characters += (
                string.ascii_letters
            )  # Add normal characters (uppercase and lowercase) to the character pool

        # Generate the password by randomly selecting characters from the character pool
        password = "".join(random.choice(characters) for i in range(int(length)))

        return password
