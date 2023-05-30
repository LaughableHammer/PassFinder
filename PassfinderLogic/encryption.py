# inspiration from https://www.tutorialspoint.com/cryptography_with_python/cryptography_with_python_caesar_cipher.htm


class Encrypt:
    def __init__(
        self, shift):  # takes in a param 'shift' which tells code how much to shift each character by
        self.shift = shift

    # Checks whether the character being encrypted is in the alphabet
    # Shifts the ASCII value odf the character in the positive direction
    #
    # Parameter -> char - the character being encrypted
    #
    # Returns -> the character, encrypted

    def shift_character(self, char):
        if char.isalpha():  # check if its in alphabet
            case_offset = (
                ord("a") if char.islower() else ord("A")
            )  # cipher only works for numbers 1-26, ascii has to be converted to be between this range and is different for uppercase or lowercase
            shifted_char = chr(
                (ord(char) - case_offset + self.shift) % 26 + case_offset
            )  # makes number in 1-26 range, shifts it by 'shift' value, places it back in its correct ascii range and converts back to char
            return shifted_char
        return char

    # Encrypts the plaintext into jargon
    # Uses the shift_character function to encrypt the characters iteratively
    #
    # Parameter -> plaintext - the text to be encrypted
    #
    # Returns -> the string (plaintext), encrypted

    def encrypt(self, plaintext):
        encrypted_text = ""  # define variable for final result
        for char in plaintext:  # loop through each character and encrypt it
            encrypted_char = self.shift_character(char)
            encrypted_text += encrypted_char
        print(encrypted_text)
        return encrypted_text  # return final value


# if __name__ == "__main__":
#     encryption = CaesarCipher(7)
#     encryption.encrypt("Kushfsdahfjsdaf")
