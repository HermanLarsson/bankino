import json
import os
from datetime import date


def transfer_money(user_id, from_account_id, to_account_id, amount):
    #Transfer money between two bank accounts
    
    # Get path to accounts file
    current_dir = os.path.dirname(__file__)
    json_path = os.path.join(current_dir, '..', '..', 'data', 'bank_accounts', 'accounts.json')
    
    # Load all accounts
    with open(json_path, 'r') as f:
        all_accounts = json.load(f)
    
    # Get accounts
    from_account = all_accounts[user_id][from_account_id]
    to_account = all_accounts[user_id][to_account_id]
    fee_account = all_accounts["4XJ38"]["ISK99TT"]
    
    # Check balance
    if from_account["balance"] >= amount + 0.25:
        # Transfer money
        from_account["balance"] -= amount + 0.25
        to_account["balance"] += amount
        fee_account["balance"] += 0.25
        
        # Add transaction
        transaction = {
            "amount": amount,
            "date": str(date.today()),
            "from_acc": from_account_id,
            "to_acc": to_account_id
        }
        
        from_account["transactions"].append(transaction)
        to_account["transactions"].append(transaction)
        
        # Save all changes back to file
        with open(json_path, 'w') as f:
            json.dump(all_accounts, f, indent=2)
        
        print(f"Success: Transferred {amount} SEK")
    else:
        print("Insufficient funds")