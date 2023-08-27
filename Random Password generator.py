# This Python program generates a random password of a specified length using the random module.
# The generate_password()
# function creates a string of all possible characters and selects randomly from it to create the password.
# The program prompts the user for the desired length and displays the generated password.

import random


def generate_password(length):
    # This contains all possible characters for the password,
    # including lowercase and uppercase letters, digits, and special characters.
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()'
    password = ''
    for _ in range(length):
        password += random.choice(characters)
    return password


# """Prompts the user for the desired password length and generates a password."""
length = int(input('Enter the desired password length: '))
password = generate_password(length)
print('Your password is:', password)
