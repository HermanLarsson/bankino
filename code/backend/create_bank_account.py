from datetime import date
import string, random, json, os

CHARACTERS = list(string.ascii_uppercase + string.digits)

#Gets the root path for any file
def get_file_path(file):
    DIRECTORY = os.path.dirname(os.path.abspath(__file__))
    file_path = DIRECTORY + "/" + file
    return file_path


#Gets the user info from the users.json file
def get_user_info(personal_num):

    file_path = get_file_path("../data/users/users.json")
    with open(file_path, "r", encoding="UTF-8") as jsonfile:
        all_users = json.load(jsonfile)

        for key in all_users:
            if all_users[key]["personal_number"] == personal_num:
                return all_users[key]


#Creates an account id
def create_account_id(bank_accounts, account_type, CHARACTERS):
    
    AMOUNT_CHARACTERS = 4 #How many characters should come after the account type
    counter = 0

    while counter != 1:
        account_id = ""
        account_id += account_type

        for i in range(AMOUNT_CHARACTERS):
            account_id += random.choice(CHARACTERS)

        if account_id not in bank_accounts:
            counter = 1
        
    return account_id


#Gets todays date
def get_date():
    todays_date = date.today()
    return todays_date



def add_new_account(account_id, today_date, user_id, account_name):

    #Saves the current accounts file in variable
    file_path = get_file_path("../data/bank_accounts/accounts.json")
    with open(file_path, "r", encoding="UTF-8") as jsonfile:
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
    
        

#Writing to the json file
def write_to_json(file, new_account):
    file_path = get_file_path(file)

    with open(file_path, "w", encoding="UTF-8") as jsonfile:
        json.dump(new_account, jsonfile, indent = 4)




def create_new_account(personal_number, account_type, account_name): #The personal number should be saved in a variable when logging in and the account_type and account_name should be inputs.

    user_info = get_user_info(personal_number)
    account_id = create_account_id(user_info["bank_accounts"], account_type, CHARACTERS) 
    today_date = get_date() 

    all_accounts = add_new_account(account_id, today_date, user_info["user_id"], account_name)
    write_to_json("../data/bank_accounts/accounts.json", all_accounts)