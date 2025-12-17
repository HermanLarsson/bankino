from datetime import date
import string, random
import backend.db_queries as db_queries
import backend.generate_card as generate_card

CHARACTERS = list(string.ascii_uppercase + string.digits)


#Creates an account id (type of account:3 uppercase letters, 4 random from list of uppercase letter and digit)
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


def create_new_account(account_type, account_name, card):
    try:
        user_id = db_queries.get_logged_in_user()
        user_info = db_queries.get_user_info(user_id)
        account_id = create_account_id(user_info["bank_accounts"], account_type, CHARACTERS) 

        updated_accounts = db_queries.update_accounts_dict(account_id, user_info["user_id"], account_name)
        db_queries.write_to_accounts_json(updated_accounts)
        updated_users = db_queries.add_new_account_to_users(user_id, account_id)
        db_queries.write_to_users_json(updated_users)
        if card == True:
            first_name, middle_name, last_name = db_queries.get_name(user_id)
            generate_card.create_card(user_id, account_id, first_name, middle_name, last_name)
        return True

    except Exception as e:
        print(f"Error: {e}")

    return False