import random
import string

def generate_password(length, use_numbers=True, use_special=True):
    characters = string.ascii_letters

    if use_numbers:
        characters += string.digits

    if use_special:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def password_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1

    if score <= 2:
        return "Weak"
    elif score == 3 or score == 4:
        return "Medium"
    else:
        return "Strong"


while True:
    print("\n====== PASSWORD GENERATOR ======")
    print("1. Generate Password")
    print("2. Generate Multiple Passwords")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        length = int(input("Enter password length: "))

        numbers = input("Include numbers? (y/n): ").lower() == "y"
        special = input("Include special characters? (y/n): ").lower() == "y"

        password = generate_password(length, numbers, special)

        print("\nGenerated Password:", password)
        print("Strength:", password_strength(password))

        save = input("Save password to file? (y/n): ").lower()

        if save == "y":
            with open("passwords.txt", "a") as file:
                file.write(password + "\n")
            print("Password saved in passwords.txt")

    elif choice == "2":
        count = int(input("How many passwords? "))
        length = int(input("Password length: "))

        numbers = input("Include numbers? (y/n): ").lower() == "y"
        special = input("Include special characters? (y/n): ").lower() == "y"

        print("\nGenerated Passwords\n")

        for i in range(count):
            password = generate_password(length, numbers, special)
            print(f"{i+1}. {password}")

    elif choice == "3":
        print("Thank you for using Password Generator!")
        break

    else:
        print("Invalid choice.")