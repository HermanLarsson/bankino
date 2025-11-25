import json

# Take the user ID to access their data in the bank_accounts JSON DB.

# hardcoded inputs for now
user_id = "A7P91"
account_id = "CHK12AB"


# Fetches all account data based on user_id
def get_all_account_data(user_id):
    with open ("./data/bank_accounts/accounts.json", "r") as file: 
        accounts = json.load(file)

        user_data = accounts[user_id]
        print(user_data)
        return user_data


# Then take a Bank ID to access the specific bank account details. 
def show_account_data(user_id, account_id):
    all_accounts = get_all_account_data(user_id)

    account_data = all_accounts[account_id]

    print(f'''Account ID: {account_data['account_id']}
Balance: {account_data['balance']}
--------------------------------
Account Name: {account_data['account_name']}
Account Type: {account_data['account_type']}
Currency: {account_data['currency']}''')

show_account_data(user_id, "CHK12AB")

# display the banks details on the screen. 
