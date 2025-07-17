'''
Strong Password Detection
Write a function that uses regular expressions to make sure the password string
it is passed is strong. A strong password has several rules:
it must be at least eight characters long, 
contain both uppercase and lowercase characters, 
and have at least one digit. Hint: 
It’s easier to test the string against multiple regex patterns than to try to come up 
with a single regex that can validate all the rules.
'''

import re, getpass

def check_password(text):
    length_symbol_pattern = re.compile(r'^[a-zA-Z0-9@!_*/.-]{8,}$')
    uppercase_pattern = re.compile(r'[A-Z]')
    lowercase_pattern = re.compile(r'[a-z]')
    digits_pattern = re.compile(r'\d')

    is_length_symbol_chars = bool(length_symbol_pattern.fullmatch(text))
    is_uppercase_chars = bool(uppercase_pattern.search(text))
    is_lowercase_chars = bool(lowercase_pattern.search(text))
    is_digits_chars = bool(digits_pattern.search(text))

    return is_length_symbol_chars and is_uppercase_chars and is_lowercase_chars and is_digits_chars

while True:
    print('Please enter your password for verfication: ')
    user_input = input('Type "quit" to exit the program: ')
    if user_input.lower() == 'quit':
        print('Exiting the program.')
        break
    
    user_password = getpass.getpass('Password (input hidden): ')
    if not user_password:
        print('Password cannot be empty.')
        continue
    if check_password(user_password):
        print('Strong password.')
    else:
        print('Password is WEAK. Please ensure it meets all criteria:')
        print('  - At least 8 characters long.')
        print('  - Contains only allowed characters (alphanumeric, @, !, _, *, /, -, .).')
        print('  - Contains at least one uppercase letter.')
        print('  - Contains at least one lowercase letter.')
        print('  - Contains at least one digit.')