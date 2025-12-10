import random, json, os
import backend.password_checker as password_checker
from datetime import date

# Global paths used in all functions.
BASE_DIR = os.path.dirname(__file__)
USERS_PATH = os.path.abspath(os.path.join(BASE_DIR, "..", "..", "data", "users", "users.json"))
BANK_ACCOUNT_PATH = os.path.abspath(os.path.join(BASE_DIR, "..", "..", "data", "bank_accounts", "accounts.json"))
CARDS_PATH = os.path.abspath(os.path.join(BASE_DIR, "..", "..", "data", "account_cards", "cards.json"))

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

def add_new_account_to_accounts(account_id, today_date, user_id, account_name):

    with open(BANK_ACCOUNT_PATH, "r", encoding="UTF-8") as jsonfile:
        all_accounts = json.load(jsonfile)
        
        #Checks if user already exist in file
        if user_id not in all_accounts.keys():
            all_accounts[user_id] = dict()

    #Adds the new account info to the variable
    all_accounts[user_id][account_id] = dict()
    all_accounts[user_id][account_id]["account_id"] = account_id
    all_accounts[user_id][account_id]["account_type"] = account_id[:3]
    all_accounts[user_id][account_id]["is_locked"] = False
    all_accounts[user_id][account_id]["account_name"] = account_name
    all_accounts[user_id][account_id]["balance"] = 0.0
    all_accounts[user_id][account_id]["currency"] = "SEK"
    all_accounts[user_id][account_id]["date_created"] = str(today_date)  
    all_accounts[user_id][account_id]["user_id"] = user_id
    all_accounts[user_id][account_id]["transactions"] = []
    all_accounts[user_id][account_id]["card_connected"] = False
    all_accounts[user_id][account_id]["card_number"] = ""

    return all_accounts

def add_new_account_to_users(user_id, new_bank_account):
    with open(USERS_PATH, "r", encoding="UTF-8") as jsonfile:
        all_accounts = json.load(jsonfile)

    all_accounts[user_id]['bank_accounts'].append(new_bank_account)
    return all_accounts
    

def write_to_accounts_json(updated_data):
    with open(BANK_ACCOUNT_PATH, "w", encoding="UTF-8") as jsonfile:
        json.dump(updated_data, jsonfile, indent = 4)


def write_to_users_json(updated_data):
    with open(USERS_PATH, "w", encoding="UTF-8") as jsonfile:
        json.dump(updated_data, jsonfile, indent = 2)

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
        "personal_number": int(personal_number),
        "join_date": join_date,
        "user_id": new_id,
        "bank_accounts": [],
        "password": password_checker.hash_password(password),
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

    # open and save the whole accounts.json file
    try:
        with open(BANK_ACCOUNT_PATH, "r", encoding="UTF-8") as file:
            accounts = json.load(file)
    except FileNotFoundError:
        print("Error: bank account database file not found.")
        return
    
    if user_id not in accounts:
        print(f'User "{user_id}" not found in database')
        return
    if bank_id not in accounts[user_id]:
        print(f'User "{user_id}" does not have an account "{bank_id}" in the database')

    # access the account to be updated
    account_to_update = accounts[user_id][bank_id]

    try:
        # add the amount to the existing balance and store the new dictionary w/ updated account balance
        account_to_update['balance'] += amount
        updated_acount_data = accounts

        transaction = {
            "amount": amount,
            "date": str(date.today()),
            "from_acc": "DEPOSIT",
            "to_acc": bank_id
        }

        updated_acount_data[user_id][bank_id]["transactions"].append(transaction)
    except TypeError:
        print("Amount must be an int")
        return

    try:
        # write the updated data back into the accounts.json file
        with open(BANK_ACCOUNT_PATH, "w", encoding="UTF-8") as file:
            json.dump(updated_acount_data, file, indent=2)
    except FileNotFoundError:
        print("Error: Bank account database file not found.")
        return


# Load all bank accounts

def load_all_bank_accounts():
    # Load all bank accounts from the JSON file
    data = {}
    try:
        f = open("./data/bank_accounts/accounts.json")
        data = json.load(f)
        f.close()
    except FileNotFoundError:
        print("Database file not found")
    
    return data

# Checks if receiving account exist in database 
def check_account_exists(account_id):
    try: 
        with open("./data/bank_accounts/accounts.json", "r") as file:
            all_accounts = json.load(file)
    except FileNotFoundError:
        print("Database file not found")
        return

    for user in all_accounts:
        if account_id in all_accounts[user]:
            return True
        

def toggle_locked_account(user_id, account_id):
    all_accounts = load_all_bank_accounts()
    chosen_account = all_accounts[user_id][account_id]

    if chosen_account['is_locked'] == True:
        chosen_account['is_locked'] = False
    else:
        chosen_account['is_locked'] = True

    write_to_accounts_json(all_accounts)
    print(f"Is locked status: {chosen_account['is_locked']}")
    return chosen_account['is_locked']


# Load all cards
def load_all_cards():
    with open(CARDS_PATH, "r", encoding="UTF-8") as users:
        all_users = json.load(users)
    return all_users


# Laod all card numbers
def load_all_card_numbers():
    all_users = load_all_cards()
    all_card_numbers = []
    for user_id, cards in all_users.items():
        for card_number, card_data in cards.items():
            all_card_numbers.append(card_data["card_number"])
    return all_card_numbers


# Write the cards data to the cards.json
def add_card_to_cards_file(all_cards):
    with open(CARDS_PATH, "w", encoding="UTF-8") as cards_file:
        json.dump(all_cards, cards_file, indent=2)


# Write the acount data to the accounts.json
def write_accounts_to_file(all_accounts):
    with open(BANK_ACCOUNT_PATH, "w", encoding="UTF-8") as accounts_file:
        json.dump(all_accounts, accounts_file, indent=2)


# Returns the first name, middle name, and last name of a user
def get_name(user_id):
    with open(USERS_PATH, "r", encoding="UTF-8") as jsonfile:
        all_users = json.load(jsonfile)
    user = all_users[user_id]
    return {
        "first_name": user["first_name"],
        "middle_name": user["middle_name"],
        "last_name": user["last_name"]
    }