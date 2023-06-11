# inspiration from https://www.tutorialspoint.com/cryptography_with_python/cryptography_with_python_caesar_cipher.htm


class Encrypt:
    def __init__(
        self, shift
    ):  # takes in a param 'shift' which tells code how much to shift each character by
        self.shift = shift


    def shift_character(self, char):
        """shifts the ascii value of a character by shift value

        Args:
            char (an ascii character): the character to be shifted

        Returns:
            char: the shifted (encrypted) character
        """
        if char.isalpha():  # check if its in alphabet
            case_offset = (
                ord("a") if char.islower() else ord("A")
            )  # cipher only works for numbers 1-26, ascii has to be converted to be between this range and is different for uppercase or lowercase
            shifted_char = chr(
                (ord(char) - case_offset + self.shift) % 26 + case_offset
            )  # makes number in 1-26 range, shifts it by 'shift' value, places it back in its correct ascii range and converts back to char
            return shifted_char
        return char
    
    def encrypt(self, plaintext):
        """Obfuscates the plaintext

        Args:
            plaintext (string): the string to be encrypted

        Returns:
            encrypted_text: the obfuscated input text
        """
        encrypted_text = ""  # define variable for final result
        for char in plaintext:  # loop through each character and encrypt it
            encrypted_char = self.shift_character(char)
            encrypted_text += encrypted_char
        print(encrypted_text)
        return encrypted_text  # return final value