import random
import string

def generate_password(length=12, use_symbols=True):
    """Generate a random password of the specified length"""
    # Define the character sets to use for each type of character
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation if use_symbols else ""

    # Combine the character sets into a single set of characters
    all_chars = lowercase_letters + uppercase_letters + digits + symbols

    # Generate a password by randomly selecting characters from the combined set
    password = "".join(random.choice(all_chars) for i in range(length))

    return password
