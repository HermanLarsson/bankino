import random, string
import backend.db_queries as db_queries
from datetime import date

DIGITS = list(string.digits)

# Generate random 16-digit string starting with 1213
def generate_card_number():
    # Load all card numbers
    existing_card_numbers = db_queries.load_all_card_numbers()

    # first 4 digits for Bankino card numbers
    BANKINO_SPECIAL_NUMBERS = "1213"
    AMOUNT_CHARACTERS = 12

    generated_card_number = BANKINO_SPECIAL_NUMBERS
    for i in range(AMOUNT_CHARACTERS):
        generated_card_number += random.choice(DIGITS)

    # Check if same card number does not exist
    if generated_card_number in existing_card_numbers:
        return generate_card_number()
    else:
        return generated_card_number
    

# Generate a random 3-digit security code
def generate_security_code():
    AMOUNT_CHARACTERS = 3
    security_code = ""
    for i in range(AMOUNT_CHARACTERS):
        security_code += random.choice(DIGITS)
        
    return security_code


# Save a new card to the JSON files
def update_cards_json(user_id, account_id, card_number, expiration_date, security_code, first_name, middle_name, last_name):
  
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

    db_queries.write_to_cards_json(all_cards)

def update_accounts_json(user_id, account_id, card_number):
    all_accounts = db_queries.get_bank_accounts()
    
    # Update the account with card information
    all_accounts[user_id][account_id]["card_connected"] = True
    all_accounts[user_id][account_id]["card_number"] = card_number
    
    db_queries.write_to_accounts_json(all_accounts)

# Generate expiration date (5 years from now)
def generate_expiration_date():
    today = date.today()
    expiration_year = today.year + 5
    expiration_date = f"{str(expiration_year)[2:]}-{today.month:02d}"
    return expiration_date

    
# Create a new card with generated card number, expiration date, and security code
def create_card(user_id, account_id):
    try:
        first_name, middle_name, last_name = db_queries.get_name(user_id)
        card_number = generate_card_number()
        expiration_date = generate_expiration_date()
        security_code = generate_security_code()

        update_cards_json(user_id, account_id, card_number, expiration_date, security_code, first_name, middle_name, last_name)
        update_accounts_json(user_id, account_id, card_number)
    except Exception as e:
        print(f"Error: {e}")