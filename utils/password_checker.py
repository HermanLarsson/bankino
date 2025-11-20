import hashlib
import json

def hash_password(user_input):
    try:
        hash = hashlib.new("SHA256")
        hash.update(user_input.encode())
        hashed_password = hash.hexdigest()

        return hashed_password
    except Exception:
        raise RuntimeError("Failed to hash password")

# Compares a hashed password to the hashed password in the db based on personal_number. 
def verify_user(personal_number, hashed_password):
    try:
        with open ("./data/users/users.json", "r") as file:
            all_users = json.load(file)
    except FileNotFoundError:
        print("Error: User database file not found.")
        return False

    for user_data in all_users.values():
        if "personal_number" not in user_data or "password" not in user_data:
            print("Error: Data mssing from users")
            return False
        elif user_data["personal_number"] == personal_number and user_data["password"] == hashed_password:
            return True

# example of how program could work...

# take a user inputted password and personal_number
personal_number = int(input("Enter personnummer: "))
user_password = input("Enter password: ")

hashed_password = hash_password(user_password)

if verify_user(personal_number, hashed_password):
    print("Login successful.")
else:
    print("Invalid credentials.")