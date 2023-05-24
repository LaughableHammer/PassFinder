class CaesarCipher:
    def __init__(self, shift):
        self.shift = shift

    def shift_character(self, char):
        if char.isalpha(): # check if its in alphabet
            case_offset = ord('a') if char.islower() else ord('A') # cipher only works for numbers 1-26, ascii has to be converted to be between this range and is different for uppercase or lowercase
            shifted_char = chr((ord(char) - case_offset + self.shift) % 26 + case_offset) # makes number in 1-26 range, shifts it by 'shift' value, places it back in its correct ascii range and converts back to char
            return shifted_char
        return char
    
    def encrypt(self, plaintext):
        encrypted_text = ""  # define variable for final result
        for char in plaintext: #loop through each character and encrypt it
            encrypted_char = self.shift_character(char)
            encrypted_text += encrypted_char
        return encrypted_text # return final value


if __name__ == "__main__":
    encryption = CaesarCipher(7)
    encryption.encrypt()