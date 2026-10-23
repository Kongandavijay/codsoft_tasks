
import secrets
import string

print("===== PASSWORD GENERATOR =====")

try:
    length = int(input("Enter password length (minimum 8): "))

    if length < 8:
        print("Please enter a length of at least 8 characters.")
    else:
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(
            secrets.choice(characters) for _ in range(length)
        )

        print("Generated password:", password)

except ValueError:
    print("Please enter a valid whole number.")
