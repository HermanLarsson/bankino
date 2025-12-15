import random
import backend.db_queries as db_queries
from datetime import date

# Gets todays date
def get_date():
    todays_date = date.today()
    return todays_date

# Generate random 16-digit number starting with 1213
def generate_card_number():
    # Load all card numbers
    existing_card_numbers = db_queries.load_all_card_numbers()

    # first 4 digits for Bankino cards
    bankino_special_numbers = "1213"
    numbers = "0123456789"
    generated_card_number = bankino_special_numbers
    for _ in range(12):
        generated_card_number += random.choice(numbers)

    # Check if same card number does not exist
    if generated_card_number in existing_card_numbers:
        return generate_card_number()
    else:
        return generated_card_number
    

# Generate a random 3-digit security code
def generate_security_code():
    numbers = "0123456789"
    security_code = random.choice(numbers) + random.choice(numbers) + random.choice(numbers) 
    return security_code


# Save a new card to the JSON files
def save_card(user_id, account_id, card_number, expiration_date, security_code, first_name, last_name, middle_name):
  
    # Load existing cards
    all_cards = db_queries.get_cards()
    user_id = str(user_id)

    # Create new card data
    new_card = {
        "account_id": str(account_id),
        "card_number": str(card_number),
        "cardholder_first_name": str(first_name),
        "cardholder_last_name": str(last_name),
        "cardholder_middle_name": str(middle_name),
        "expiration_date": str(expiration_date),
        "security_code": str(security_code)
    }
    # Check if user already exists in the file
    if user_id not in all_cards:
        all_cards[user_id] = {}
    all_cards[user_id][card_number] = new_card

    # Load existing accounts
    all_accounts = db_queries.get_bank_accounts()
    
    # Update the account with card information
    all_accounts[user_id][account_id]["card_connected"] = True
    all_accounts[user_id][account_id]["card_number"] = card_number
    
    # Write to both files
    db_queries.write_to_cards_json(all_cards)
    db_queries.write_to_accounts_json(all_accounts)


# Create a new card with generated card number, expiration date, and security code
def create_card(user_id, account_id, first_name, last_name, middle_name):
    
    
    # Generate unique card number
    card_number = generate_card_number()
    
    # Generate expiration date (5 years from now)
    today = get_date()
    expiration_year = today.year + 5
    expiration_date = f"{str(expiration_year)[2:]}-{today.month:02d}"
    
    # Generate random 3-digit security code
    security_code = generate_security_code()
    
    save_card(user_id, account_id, card_number, expiration_date, security_code, first_name, last_name, middle_name)

