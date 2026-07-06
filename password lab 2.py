import string
import secrets

def generate_password():
    print("=== Secure Password Generator ===")

    # Step 1: Ask user for password requirements
    length = int(input("Enter the desired password length: "))

    include_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
    include_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
    include_digits = input("Include digits? (y/n): ").lower() == 'y'
    include_special = input("Include special characters? (y/n): ").lower() == 'y'
# Step 2: Build character pool based on user input
    characters = ''
    if include_upper:
        characters += string.ascii_uppercase
    if include_lower:
        characters += string.ascii_lowercase
    if include_digits:
        characters += string.digits
    if include_special:
        characters += string.punctuation

    # Step 3: Validate that user selected at least one character type
    if not characters:
        print("You must select at least one type of character!")
        return

    # Step 4: Generate a random password securely
    password = ''.join(secrets.choice(characters) for _ in range(length))

    print(f"\n Your secure password is: {password}")
generate_password()
