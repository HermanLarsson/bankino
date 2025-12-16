import random, json, os
import backend.password_checker as password_checker
from datetime import date

# Global paths used in all functions.
BASE_DIR = os.path.dirname(__file__)
USERS_PATH = os.path.abspath(os.path.join(BASE_DIR, "..", "..", "data", "users", "users.json"))
BANK_ACCOUNT_PATH = os.path.abspath(os.path.join(BASE_DIR, "..", "..", "data", "bank_accounts", "accounts.json"))
CARDS_PATH = os.path.abspath(os.path.join(BASE_DIR, "..", "..", "data", "account_cards", "cards.json"))

# Fetches whole accounts.json file
def get_bank_accounts():
    try:
        with open(BANK_ACCOUNT_PATH, "r", encoding="UTF-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print("File not found")
    return {}


# Fetches whole users.json file
def get_users():
    try: 
        with open(USERS_PATH, "r", encoding="UTF-8") as file:
            return json.load(file)
    except FileExistsError:
        print("File not found")
    return {}


# Fetch while cards.json file
def get_cards():
    try:
        with open(CARDS_PATH, "r", encoding="UTF-8") as cards:
            return json.load(cards)
    except FileExistsError:
        print("File not found")
    return {}


# Fetches the accounts of a specific user
def get_user_bank_accounts(user_id):
    all_accounts = get_bank_accounts()
    try:
        return all_accounts[user_id]
    except KeyError:
        print(f"User {user_id} not in Database")
    return {}


# Takes a user id and returns dictionary with their account information
def get_user_info(user_id):
    all_users = get_users()
    try:
        return all_users[user_id]
    except KeyError:
        print(f"User_id {user_id} does not exist in the database")
    return {}

# Take a user id and returns a dictionary with all of their specific bank account details
def get_bank_accounts_by_user(user_id):
    all_accounts = get_bank_accounts()
    try:
        return all_accounts[user_id]
    except KeyError:
        print(f"User {user_id}'s bank account data does not exist in the database")
    return {}


# Return the user_id of the user currntly logged in. 
def get_logged_in_user():
    try:
        with open ("./data/cache/logged_in_user.cache", "r") as file:
            logged_in_user = file.read()
            if logged_in_user == "":
                print("No users logged in")
                return ""
            else:
                print(f"Logged in user: {logged_in_user}")
                return logged_in_user
    except FileNotFoundError:
            print("Main could not find cachefile")
    return ""


# Takes account_id, todays date (Formatted: YYYY-MM-DD), user_id, and account name given by user.
# Returns the whole accounts file with the new account added.  
def update_accounts_dict(account_id, user_id, account_name):
    all_accounts = get_bank_accounts()
        
    #Checks if user already exist in file
    if user_id not in all_accounts.keys():
        all_accounts[user_id] = dict()

    #Adds the new account info to the variable
    all_accounts[user_id][account_id] = dict()
    all_accounts[user_id][account_id]["account_id"] = account_id
    all_accounts[user_id][account_id]["account_type"] = account_id[:3]
    all_accounts[user_id][account_id]["is_locked"] = False
    all_accounts[user_id][account_id]["locked_until_date"] = ""
    all_accounts[user_id][account_id]["account_name"] = account_name
    all_accounts[user_id][account_id]["balance"] = 0.0
    all_accounts[user_id][account_id]["currency"] = "SEK"
    all_accounts[user_id][account_id]["date_created"] = str(date.today()) 
    all_accounts[user_id][account_id]["user_id"] = user_id
    all_accounts[user_id][account_id]["transactions"] = []
    all_accounts[user_id][account_id]["card_connected"] = False
    all_accounts[user_id][account_id]["card_number"] = ""

    return all_accounts

# Returns the whole users file with the new account_id added to bank_accounts.  
def add_new_account_to_users(user_id, new_bank_account):
    all_users = get_users()
    try: 
        all_users[user_id]['bank_accounts'].append(new_bank_account)
        return all_users
    except KeyError:
        print(f"User {user_id} does not exist in database")
    return {}
    

# Takes an updated accounts dictionary and writes it to the accounts.json file, overriding the existing data.
def write_to_accounts_json(updated_data):
    try: 
        with open(BANK_ACCOUNT_PATH, "w", encoding="UTF-8") as jsonfile:
            json.dump(updated_data, jsonfile, indent = 4)
        return True
    except FileExistsError:
        print("File not found")
    return False


# Takes an updated users dictionary and writes it to the users.json file, overriding the existing data.
def write_to_users_json(updated_data):
    try: 
        with open(USERS_PATH, "w", encoding="UTF-8") as jsonfile:
            json.dump(updated_data, jsonfile, indent = 2)
        return True
    except FileNotFoundError: 
        print("File not found")
    return False


# Write the cards data to the cards.json
def write_to_cards_json(all_cards):
    try: 
        with open(CARDS_PATH, "w", encoding="UTF-8") as cards_file:
            json.dump(all_cards, cards_file, indent=2)
        return True
    except FileNotFoundError:
        print("File not found")
    return False



# Creates and returns a unique user_id. 
def generate_user_id():
    all_users = get_users()
    existing_ids = all_users.keys()

    # Generate random id: number + letter + letter + number + number
    numbers = "0123456789"
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    generated_id = random.choice(numbers) + random.choice(letters) + random.choice(letters) + random.choice(numbers) + random.choice(numbers)

    # Check if same id does not already exist
    if generated_id in existing_ids:
        return generate_user_id()
    else:
        return generated_id
    

# Creates a dictionary of user data and writes the updated data to the database.
# TODO: we should change join date in future
def sign_up(first_name, last_name, middle_name, personal_number, join_date, password):
    try:
        new_id = generate_user_id()

        user_data = {
            "first_name": first_name,
            "last_name": last_name,
            "middle_name": middle_name,
            "personal_number": int(personal_number),
            "join_date": join_date,
            "user_id": new_id,
            "bank_accounts": [],
            "password": password,
        }

        all_users = get_users()
        all_users[new_id] = user_data
        write_to_users_json(all_users)
        return True
    except:
        print("Error occured while signing up user")
    return False


# Checks the inputted personal number and password against the users database
# if personal number and password match a user in the DB, their user_id is returned
def verify_user(personal_number, hashed_password):
    all_users = get_users()
    output = ""
    
    for user_data in all_users.values():
        if (user_data['personal_number'] == int(personal_number)) and user_data['password'] == hashed_password:
            output = user_data["user_id"]

    return output


# Updates the balance of the account involved in the transaction and writes the transaction to the database
def deposit_funds(user_id, account_id, amount):
    all_accounts = get_bank_accounts()
    
    if user_id not in all_accounts:
        print(f'User "{user_id}" not found in database')
        return False

    # Access the account to be updated and update the balance
    try:
        all_accounts[user_id][account_id]['balance'] += amount
    except KeyError:
        print(f"User {user_id} does not have the account {account_id}")
        return False

    # Create the transaction data
    transaction = {
        "amount": amount,
        "date": str(date.today()),
        "from_acc": "DEPOSIT",
        "to_acc": account_id
    }

    all_accounts[user_id][account_id]["transactions"].append(transaction)

    # Write updated data to the database
    write_to_accounts_json(all_accounts)
    return True


# Checks if receiving account exist in database
def check_account_exists(account_id):
    try: 
        all_accounts = get_bank_accounts()

        for user in all_accounts:
            if account_id in all_accounts[user]:
                return True
    except:
        print("Error occured while checking if account exists")
    return False

# Toggles the value of 'is_locked' between true and false
def toggle_locked_account(user_id, account_id):
    try: 
        all_accounts = get_bank_accounts()
        chosen_account = all_accounts[user_id][account_id]

        chosen_account['is_locked'] = not chosen_account['is_locked']
    except KeyError:
        print("Account not in Database")
        return "Toggle Unsuccessful"

    if write_to_accounts_json(all_accounts):
        print(f"Is locked status: {chosen_account['is_locked']}")
        return "Toggle Successful"
    else:
        return "Toggle Unseccessful"



# Iterates through whole cards.json and returns a list of all card numbers for all users. 
# Used to check that newly generated cards numbers don't already exist. 
def load_all_card_numbers():
    all_cards = get_cards()
    all_card_numbers = []
    for cards in all_cards.values():
        for card_number in cards.keys():
            all_card_numbers.append(card_number)
    return all_card_numbers



# Returns the first name, middle name, and last name of a user
def get_name(user_id):
    user = get_user_info(user_id)
    return user["first_name"], user["middle_name"], user["last_name"]


# Reduces the balance of a chosen account by 100. Writes changes to Database
def fine_user(user_id, account_id):
    try: 
        all_accounts = get_bank_accounts()
        chosen_account = all_accounts[user_id][account_id]
        # Constant amount to be fined = 100kr
        FINE = 100
        chosen_account['balance'] -= FINE
        write_to_accounts_json(all_accounts)
        return True
    except:
        print("Error occured while processing fine")
    return False


# Takes a user and a dictionary of user information and overwrites the data for that user. 
# Returns True if update is successful, otherwise false.
def update_user_info(user_id, new_info):
    try: 
        all_users = get_users()
        for input in new_info.keys():
            all_users[user_id][input] = new_info[input]
        
        write_to_users_json(all_users)
        return True
    except KeyError:
        print(f"User {user_id} does not exist in the Database")

    return False

    
# Takes a user_id and an account_id and removes bank account from accounts.json 
def delete_bank_account(user_id, account_id):
    try:
        all_bank_accounts = get_bank_accounts()

        # Remove from cards.json
        if all_bank_accounts[user_id][account_id]["card_connected"]:
            card_number = all_bank_accounts[user_id][account_id]["card_number"]

            all_cards = get_cards()
            all_cards[user_id].pop(card_number)
            write_to_cards_json(all_cards)

        # Remove from accounts.json
        all_bank_accounts[user_id].pop(account_id)
        write_to_accounts_json(all_bank_accounts)

        # Remove from users.json
        all_users = get_users()
        all_users[user_id]["bank_accounts"].remove(account_id)
        write_to_users_json(all_users)
        return True
    except:
        print("Error while removing bank account from accounts.json")
    return False
        
