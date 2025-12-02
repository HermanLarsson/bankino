import random, json, os

# Global paths used in all functions.
BASE_DIR = os.path.dirname(__file__)
USERS_PATH = os.path.abspath(os.path.join(BASE_DIR, "..", "..", "data", "users", "users.json"))
BANK_ACCOUNT_PATH = os.path.abspath(os.path.join(BASE_DIR, "..", "..", "data", "bank_accounts", "accounts.json"))


# Create bankaccount

def get_user_info(user_id):
    with open(USERS_PATH, "r", encoding="UTF-8") as jsonfile:
        all_users = json.load(jsonfile)

        return all_users[user_id]

def get_user_id():
    try:
            with open ("./data/cache/logged_in_user.cache", "r") as file:
                logged_in_user = file.read()
                print(logged_in_user)
                return logged_in_user
    except FileNotFoundError:
            print("Main could not find cachefile")

def add_new_account(account_id, today_date, user_id, account_name):

    with open(BANK_ACCOUNT_PATH, "r", encoding="UTF-8") as jsonfile:
        all_accounts = json.load(jsonfile)
        
        #Checks if user already exist in file
        if user_id not in all_accounts.keys():
            all_accounts[user_id][account_id] = dict()

    #Adds the new account info to the variable
    all_accounts[user_id][account_id] = dict()
    all_accounts[user_id][account_id]["account_id"] = account_id
    all_accounts[user_id][account_id]["account_type"] = account_id[:3]
    all_accounts[user_id][account_id]["account_name"] = account_name
    all_accounts[user_id][account_id]["balance"] = 0.0
    all_accounts[user_id][account_id]["currency"] = "SEK"
    all_accounts[user_id][account_id]["date_created"] = str(today_date)  
    all_accounts[user_id][account_id]["user_id"] = user_id
    all_accounts[user_id][account_id]["transactions"] = []
    all_accounts[user_id][account_id]["card_connected"] = False
    all_accounts[user_id][account_id]["card_number"] = ""

    return all_accounts
    
def write_to_json(new_account):

    with open(BANK_ACCOUNT_PATH, "w", encoding="UTF-8") as jsonfile:
        json.dump(new_account, jsonfile, indent = 4)


# Signup user

def generate_user_id():

    #Load existing users to check if id does not exist
    with open(USERS_PATH, "r") as users:
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


    with open(USERS_PATH, "r") as old_users:
        all_users = json.load(old_users)
    
    all_users[new_id] = user_data
    
    with open(USERS_PATH, "w") as new_users:
        json.dump(all_users , new_users , indent=2)


# Bank account window

def get_all_account_data(user_id):
    try: 
        with open ("./data/bank_accounts/accounts.json", "r") as file: 
            accounts = json.load(file)
    except FileNotFoundError:
            print("Error: Accounts database file not found.")

    user_data = accounts[user_id]
    print(user_data)
    return user_data


# Landing page

def load_bank_accounts(user_id):
    try:
        f = open("./data/bank_accounts/accounts.json")
        data = json.load(f)
        f.close()
        return data[user_id]
    except FileNotFoundError:
        print("Database file not found")


# Login window

def verify_user(personal_number, hashed_password):
    try:
        print(USERS_PATH)
        with open (USERS_PATH, "r") as file:
            all_users = json.load(file)
    except FileNotFoundError:
        print("Error: User database file not found.")
        return ""
    
    output = ""
    
    for user_data in all_users.values():
        if (user_data['personal_number'] == int(personal_number)) and user_data['password'] == hashed_password:
            print("Found user!")
            output = user_data["user_id"]

    return output


# Depositing funds logic

def deposit_funds(user_id, bank_id, amount):
    updated_acount_data = None

    with open(BANK_ACCOUNT_PATH, "r", encoding="UTF-8") as file:
        accounts = json.load(file)
        account_to_update = accounts[user_id][bank_id]
        account_to_update['balance'] = account_to_update['balance'] + amount
        updated_acount_data = accounts

    with open(BANK_ACCOUNT_PATH, "w", encoding="UTF-8") as file:
        json.dump(updated_acount_data, file)


# test to see if values are updated
# deposit_funds('4XJ38', 'ISK99TT', 14559.09)