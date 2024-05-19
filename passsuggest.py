import random
import string

def generate_password(length, include_uppercase, include_numbers, include_symbols):
    # Define the character sets
    lowercase_chars = string.ascii_lowercase
    uppercase_chars = string.ascii_uppercase
    digit_chars = string.digits
    symbol_chars = string.punctuation

    # Create the character pool based on user preferences
    char_pool = lowercase_chars
    if include_uppercase:
        char_pool += uppercase_chars
    if include_numbers:
        char_pool += digit_chars
    if include_symbols:
        char_pool += symbol_chars

    # Generate the password
    password = ''.join(random.choices(char_pool, k=length))
    return password

# Get user input
password_length = int(input("Enter the desired password length: "))
include_uppercase = input("Include uppercase letters? (y/n) ").lower() == 'y'
include_numbers = input("Include numbers? (y/n) ").lower() == 'y'
include_symbols = input("Include symbols? (y/n) ").lower() == 'y'

# Generate the password
suggested_password = generate_password(password_length, include_uppercase, include_numbers, include_symbols)
print(f"Suggested password: {suggested_password}")
