from datetime import date
from backend.db_queries import get_bank_accounts, write_to_accounts_json

# Returns the path to reach the specific bank account in accounts.json
def validate_receiving_account(all_accounts, user_accounts, to_account_id):
    if to_account_id in user_accounts:
        return user_accounts[to_account_id]
    else:
        for user in all_accounts:
            if to_account_id in all_accounts[user]:
                return all_accounts[user][to_account_id]


def add_transaction_to_history(from_account, to_account, amount, transaction_date, from_account_id, to_account_id):
    # Appends the transaction to both accounts' transaction history
    
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
    try:
        all_accounts = get_bank_accounts()
        user_accounts = all_accounts[user_id]

        from_account = user_accounts[from_account_id]
        to_account = validate_receiving_account(all_accounts, user_accounts, to_account_id) 

        from_account["balance"] -= amount
        to_account["balance"] += amount

        transaction_date = str(date.today())
        add_transaction_to_history(from_account, to_account, amount, transaction_date, from_account_id, to_account_id)

        write_to_accounts_json(all_accounts)
        return True
    
    except Exception as e:
        print(f"Error: {e}")
        
    return False

def check_sufficient_funds(current_balance, withdrawal):
    if current_balance - withdrawal < 0:
        print("Insufficient funds for this transaction")
        return False
    
    return True