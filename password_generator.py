#Password Generator
#Enjoy😘

import random
import string
from termcolor import colored

def generate_password(length=12, use_digits=True, use_specials=True):
    """Generate a random password with the given length and options."""
    characters = string.ascii_letters  
    if use_digits:
        characters += string.digits
    if use_specials:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


try:
    length = int(input(colored("Enter password length (default 12): ", "cyan")) or 12)
    use_digits = input(colored("Include digits? (y/n): ", "cyan")).strip().lower() == 'y'
    use_specials = input(colored("Include special characters? (y/n): ", "cyan")).strip().lower() == 'y'


    password = generate_password(length, use_digits, use_specials)
    print(colored(f"\nGenerated Password: {password}", "green"))
except ValueError:
    print(colored("Invalid input! Please enter a valid number for length.", "red"))
