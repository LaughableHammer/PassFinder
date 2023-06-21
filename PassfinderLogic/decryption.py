# inspiration from https://www.tutorialspoint.com/cryptography_with_python/cryptography_with_python_caesar_cipher.htm


class Decrypt:
    """Decryption algorithm for the encryption algorithm"""

    def __init__(
        self,
        shift,
    ):
        self.shift = shift

    def shift_character(
        self,
        char,
        reverse=False,
    ):
        """shifts each character's ascii value by an amount

        Args:
            char (an ascii character): the character being shifted
            reverse (bool, optional): can reverse for encryption. Defaults to False.

        Returns:
            char: returns the decrypted char
        """
        if char.isalpha():  # checks if the character is in the alphabet
            case_offset = (
                ord("a") if char.islower() else ord("A")
            )  # cipher only works for numbers 1-26, ascii has to be converted to be between this range and is different for uppercase or lowercase
            shift = (
                -self.shift if reverse else self.shift
            )  # does same as encryption however extra argument for if we want to reverse
            shifted_char = chr(
                (ord(char) - case_offset + shift) % 26 + case_offset
            )  # shifts the character
            return shifted_char
        return char

    def decrypt(
        self,
        ciphertext,
    ):
        """uses shift_character to decrypt all letters of a string

        Args:
            ciphertext (string): the string to be decrypted

        Returns:
            decrypted_text: the input but decrypted
        """
        decrypted_text = ""  # final result to be returned
        for char in ciphertext:  # iterate through each character
            decrypted_char = self.shift_character(
                char, reverse=True
            )  # does same as shift character in encryption however reverses it
            decrypted_text += decrypted_char  # add decrypted character to new string
        print(decrypted_text)
        return decrypted_text  # return decrypted ciphertext
