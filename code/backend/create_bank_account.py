from datetime import date
import string, random, json, os
import backend.db_queries as db_queries
import backend.generate_card as generate_card

CHARACTERS = list(string.ascii_uppercase + string.digits)


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


def create_new_account(account_type, account_name, card): #The personal number should be saved in a variable when logging in and the account_type and account_name should be inputs.

    user_id = db_queries.get_user_id()
    user_info = db_queries.get_user_info(user_id)
    account_id = create_account_id(user_info["bank_accounts"], account_type, CHARACTERS) 
    today_date = get_date() 

    updated_accounts = db_queries.add_new_account_to_accounts(account_id, today_date, user_info["user_id"], account_name)
    db_queries.write_to_accounts_json(updated_accounts)
    updated_users = db_queries.add_new_account_to_users(user_id, account_id)
    db_queries.write_to_users_json(updated_users)
    if card == True:
        generate_card.generate_card
        return account_id
    else:
        return account_id