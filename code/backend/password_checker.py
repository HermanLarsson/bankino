import hashlib
import json
from db_queries import *

def hash_password(user_input):
    try:
        hash = hashlib.new("SHA256")
        hash.update(user_input.encode())
        hashed_password = hash.hexdigest()

        return hashed_password
    except Exception:
        raise RuntimeError("Failed to hash password")

# Compares a hashed password to the hashed password in the db based on personal_number. 
# Returns " " if the user could not be verified or logged in or not found. Returns the user_id if login is successful
