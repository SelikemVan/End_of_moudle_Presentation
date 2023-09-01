# This Python program generates a random password of a specified length using the random module.
# The generate_password()
# function creates a string of all possible characters and selects randomly from it to create the password.
# The program prompts the user for the desired length and displays the generated password.
# It utilizes the 'random' module to introduce randomness into the process
import random


def generate_password(length):
    # "characters" contains all possible characters for the password,
    # including lowercase and uppercase letters, digits, and special characters.
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()'
    # "password" stores the characters in the generation of the password
    password = ''
    # In each iteration, the loop randomly selects a character from the character's
    # string using the random.choice() function.
    for _ in range(length):
        password += random.choice(characters)
    return password


# Prompts the user for the desired password length and generates a password.
length = int(input('Enter the desired password length: '))
password = generate_password(length)
print('Your password is:', password)
