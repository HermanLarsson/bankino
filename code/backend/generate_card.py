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


# Create a new card with generated card number, expiration date, and security code
def create_card(user_id, account_id, first_name, last_name, middle_name):
    
    
    # Generate unique card number
    card_number = generate_card_number()
    
    # Generate expiration date (5 years from now)
    today = get_date()
    expiration_year = today.year + 5
    expiration_date = f"{str(expiration_year)[2:]}{today.month:02d}"
    
    # Generate random 3-digit security code
    security_code = generate_security_code()
