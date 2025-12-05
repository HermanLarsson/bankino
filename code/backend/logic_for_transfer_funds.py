from datetime import date
from backend.db_queries import load_all_bank_accounts, write_to_json


def add_transaction_to_history(user_id, from_account_id, to_account_id, amount, transaction_date, all_accounts):
    # Add a transaction record to both accounts' transaction history
    
    transaction = {
        "amount": amount,
        "date": transaction_date,
        "from_acc": from_account_id,
        "to_acc": to_account_id
    }
    
    all_accounts[user_id][from_account_id]["transactions"].append(transaction)
    all_accounts[user_id][to_account_id]["transactions"].append(transaction)


def transfer_money(user_id, from_account_id, to_account_id, amount):
    # Transfer money between two bank accounts
    
    all_accounts = load_all_bank_accounts()
    user_accounts = all_accounts[user_id]
    
    from_account = user_accounts[from_account_id]
    to_account = user_accounts[to_account_id]
    
    from_account["balance"] -= amount
    to_account["balance"] += amount
    
    transaction_date = str(date.today())
    add_transaction_to_history(user_id, from_account_id, to_account_id, amount, transaction_date, all_accounts)
    
    write_to_json(all_accounts)
