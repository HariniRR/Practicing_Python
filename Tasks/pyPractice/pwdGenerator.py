import random
import string
def generate_password(length=12, use_special=True, use_digits=True):
    characters = string.ascii_letters
    if use_special:
        characters += string.punctuation
    if use_digits:
        characters += string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
length = int(input("Enter password length: "))
special = input("Include special characters? (y/n): ").lower() == 'y'
digits = input("Include digits? (y/n): ").lower() == 'y'

print("Generated Password:", generate_password(length, special, digits))
