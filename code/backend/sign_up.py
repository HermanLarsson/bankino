import random
import json
import os


BASE_DIR = os.path.dirname(__file__)  # directory of this script
file_path = os.path.abspath(os.path.join(BASE_DIR, "..", "..", "data", "users", "users.json"))


def generate_user_id():
   
    
    #Load existing users to check if id does not exist
    with open(file_path, "r") as users:
        all_users = json.load(users)

    existing_ids = all_users.keys()

    #Generate random id: number + letter + letter + number + number
    numbers = "0123456789"
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    generated_id = random.choice(numbers) + random.choice(letters) + random.choice(letters) + random.choice(numbers) + random.choice(numbers)

    #Check if same id does not exist
    if generated_id in existing_ids:
        return generate_user_id()
    else:
        return generated_id

    
def sign_up(first_name, last_name, middle_name, personal_number, join_date, password): # we should change join date in future


    new_id = generate_user_id()


    user_data = {
        "first_name": first_name,
        "last_name": last_name,
        "middle_name": middle_name,
        "personal_number": personal_number,
        "join_date": join_date,
        "user_id": new_id,
        "bank_accounts": [],
        "password": password,
    }


    with open(file_path, "r") as old_users:
        all_users = json.load(old_users)
    
    all_users[new_id] = user_data
    
    with open(file_path, "w") as new_users:
        json.dump(all_users , new_users , indent=2)