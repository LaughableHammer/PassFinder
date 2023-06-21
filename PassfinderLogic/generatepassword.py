import random
import string


class PasswordGenerator:
    """Generates a random password using user specifications"""

    def generate_password(
        self,
        length: str,
        special_characters: bool,
        numbers: bool,
        normal_characters: bool,
    ):
        """Generates an array of characters using user specifications and then selects random characters from it

        Args:
            length (str): Length of the password (user defined)
            special_characters (bool): Whether to include special characters (user defined)
            numbers (bool): Whether to include numbers (user defined)
            normal_characters (bool): Whether to include normal ascii characters (user defined)

        Returns:
            password: The final string containing the generated password
        """
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
