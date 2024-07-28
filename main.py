import string
import random

lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digits = string.digits
special_characters = string.punctuation

def generate_password(length, use_uppercase=True, use_digits=True, use_special=True):
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

length = int(input("Enter the password length: "))
use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
use_digits = input("Include digits? (yes/no): ").lower() == 'yes'
use_special = input("Include special characters? (yes/no): ").lower() == 'yes'

password = generate_password(length, use_uppercase, use_digits, use_special)
print(f"Generated password: {password}")
