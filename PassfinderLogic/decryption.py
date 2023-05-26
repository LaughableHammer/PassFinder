# inspiration from https://www.tutorialspoint.com/cryptography_with_python/cryptography_with_python_caesar_cipher.htm


class CaesarCipher:
    def __init__(self, shift):
        self.shift = shift

    # Checks whether the character being decrypted is in the alphabet
    # Shifts the ASCII value of the character in the negative direction to the encryption
    #
    # Parameter -> char - the character being decrypted
    # Parameter -> reverse - boolean that just reverses the logic of the encryption algorithm
    #
    # Returns -> the character, decrypted

    def shift_character(self, char, reverse=False):
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

    # Creats an empty string for the output
    # Reverse the encryption on each character individually using the shift_character function
    #
    # Parameter -> ciphertext - the ciphered text that needs to be decrypted
    #
    # Returns -> the decrypted version of the ciphertext input

    def decrypt(self, ciphertext):
        decrypted_text = ""  # final result to be returned
        for char in ciphertext:  # iterate through each character
            decrypted_char = self.shift_character(
                char, reverse=True
            )  # does same as shift character in encryption however reverses it
            decrypted_text += decrypted_char  # add decrypted character to new string
        print(decrypted_text)
        return decrypted_text  # return decrypted ciphertext


if __name__ == "__main__":
    decryption = CaesarCipher(7) # 7 is the 'key'
    decryption.decrypt("Rbzomzkhomqzkhm")
