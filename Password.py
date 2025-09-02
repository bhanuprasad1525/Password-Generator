import random
import string

class PasswordGenerator:
    def __init__(self, length=12, use_digits=True, use_special=True):
        self.length = length
        self.use_digits = use_digits
        self.use_special = use_special
        self.characters = string.ascii_letters

        if self.use_digits:
            self.characters += string.digits 
        if self.use_special:
            self.characters += string.punctuation  

    def generate_password(self):
        if self.length < 4:
            raise ValueError("Password length must be at least 4 characters.")
        password = ''.join(random.choice(self.characters) for _ in range(self.length))
        return password

if __name__ == "__main__":
    print(" Welcome to Password Generator (OOP)")
    try:
        length = int(input("Enter password length (e.g. 12): "))
    except ValueError:
        print("Invalid input! Using default length 12.")
        length = 12
    digits = input("Include digits? (y/n): ").lower() == 'y'
    special = input("Include special characters? (y/n): ").lower() == 'y'
    generator = PasswordGenerator(length, digits, special)
    password = generator.generate_password()
    print(f"\n Your Generated Password: {password}")
