class CaesarCipher:
    def __init__(self, shift):
        self.shift = shift

    def shift_character(self, char, reverse=False):
        if char.isalpha(): # checks if the character is in the alphabet
            case_offset = ord('a') if char.islower() else ord('A') # cipher only works for numbers 1-26, ascii has to be converted to be between this range and is different for uppercase or lowercase
            shift = -self.shift if reverse else self.shift # does same as encryption however extra argument for if we want to reverse
            shifted_char = chr((ord(char) - case_offset + shift) % 26 + case_offset) # shifts the character
            return shifted_char
        return char

    def decrypt(self, ciphertext):
        decrypted_text = "" # final result to be returned
        for char in ciphertext: # iterate through each character
            decrypted_char = self.shift_character(char, reverse=True) # does same as shift character in encryption however reverses it
            decrypted_text += decrypted_char # add decrypted character to new string
        return decrypted_text


if __name__ == "__main__":
    decryption = CaesarCipher(7)
    decryption.decrypt()