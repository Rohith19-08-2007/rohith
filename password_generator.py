
import random
import string

def generate_password(length=12, use_digits=True, use_special=True, use_uppercase=True, use_lowercase=True):
    characters = ''
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase

    if not characters:
        raise ValueError("At least one character set must be enabled!")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def get_user_preferences():
    print("Customize your password:")
    length = int(input("Enter password length (e.g., 12): "))
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_special = input("Include special characters? (y/n): ").lower() == 'y'
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'

    try:
        password = generate_password(length, use_digits, use_special, use_uppercase, use_lowercase)
        print(f"Generated Password: {password}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    get_user_preferences()
