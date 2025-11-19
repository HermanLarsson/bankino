import hashlib
import json

# take a user inputted password and personal_number
personal_number = int(input("Enter personnummer: "))
user_password = input("Enter password: ")

def hash_password(user_input):
    hash = hashlib.new("SHA256")
    hash.update(user_input.encode())
    hashed_password = hash.hexdigest()

    return hashed_password

# Compares a hashed password to the hashed password in the db based on personal_number. 
def verify_user(personal_number, hashed_password):
    with open ("./data/users/users.json", "r") as file:
        all_users = json.load(file)
        for user_data in all_users.values():
            if user_data["personal_number"] == personal_number and user_data["password"] == hashed_password:
                return True

# example of how program could work...
hashed_password = hash_password(user_password)

if verify_user(personal_number, hashed_password):
    print("Login successful.")
else:
    print("Invalid credentials.")