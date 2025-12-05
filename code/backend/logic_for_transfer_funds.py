from datetime import date
from backend.db_queries import load_all_bank_accounts, write_to_json

def validate_receiving_account(all_accounts, user_accounts, to_account_id):
    if to_account_id in user_accounts.items():
        return user_accounts[to_account_id]
    else:
        for user_id in all_accounts:
            if to_account_id in user_id.items():
                return user_id[to_account_id]
            else:
                print("Account Not Found")


def add_transaction_to_history(from_account, to_account, amount, transaction_date, from_account_id, to_account_id):
    # Add a transaction record to both accounts' transaction history
    
    transaction = {
        "amount": amount,
        "date": transaction_date,
        "from_acc": from_account_id,
        "to_acc": to_account_id
    }
    
    from_account["transactions"].append(transaction)
    to_account["transactions"].append(transaction)


def transfer_money(user_id, from_account_id, to_account_id, amount):
    # Transfer money between two bank accounts
    
    all_accounts = load_all_bank_accounts()
    user_accounts = all_accounts[user_id]
    
    from_account = user_accounts[from_account_id]
    to_account = validate_receiving_account(all_accounts, user_accounts, to_account_id)

    from_account["balance"] -= amount
    to_account["balance"] += amount
    
    transaction_date = str(date.today())
    add_transaction_to_history(from_account, to_account, amount, transaction_date, from_account_id, to_account_id)
    
    write_to_json(all_accounts)
