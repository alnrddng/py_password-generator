# !/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Name: Random Password Generator
Purpose: A random password generator to build passwords based on the user's preferences.
Version: 20230415
License: MIT

Developer(s): Alan Redding (GitHub: alnrddng)
'''

import random

def get_user_request():
    ''' obtain the requirements from the user '''

    number_of_passwords = int(input("How many passwords do you need? (Num) "))
    password_length = int(input("How long should the passwords be (Num) "))
    include_upper = input("Would you like to include uppercase letters? (Y/N) ")
    include_lower = input("Would you like to include lowercase letters? (Y/N) ")
    include_numbers = input("Would you like to include numbers? (Y/N) ")
    include_symbols = input("Would you like to include symbols? (Y/N) ")

    return [number_of_passwords, password_length, include_upper.lower(), include_lower.lower(), include_numbers.lower(), include_symbols.lower()]

def main():
    ''' build random passwords based on the user's requirements '''

    print("Random Password Generator")
    print("================================================================")

    requirements = get_user_request()

    alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet_lower = "abcdefghijklmnopqrstuvwxyz"
    numbers = "0123456789"
    symbols = "`~!@#$%^&*()-_=+[{]};:,<.>/?"
    pool = ''

    if requirements[2] == 'y':
        pool += alphabet_upper
    if requirements[3] == 'y':
        pool += alphabet_lower
    if requirements[4] == 'y':
        pool += numbers
    if requirements[5] == 'y':
        pool += symbols

    print("Here are your passwords:")

    for x in range(requirements[0]):
        password = ''
        for c in range(requirements[1]):
            password += random.choice(pool)
        print(password)

if __name__ == "__main__":
    main()
