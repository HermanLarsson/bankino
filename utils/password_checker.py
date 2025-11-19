import hashlib
import json

# take a user inputted password and personal_number
personal_number = int(input("Enter personnummer: "))
user_password = input("Enter password: ")

# hash it
def hash_password(user_password):
    hash = hashlib.new("SHA256")
    hash.update(user_password.encode())
    hashed_password = hash.hexdigest()

    return hashed_password

# check the hashed password to the hashed password of that user in the db. 
def verify_user(personal_number, hashed_password):
    user_to_verify = None

    with open ("./data/users/users.json", "r") as file:
        all_users = json.load(file)
        for user_data in all_users.values():
            if user_data["personal_number"] == personal_number and user_data["password"] == hashed_password:
                user_to_verify = user_data

    if user_to_verify:
        return True
    else:
        return False
    

print(verify_user(personal_number, hash_password(user_password)))