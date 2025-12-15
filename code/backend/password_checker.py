import hashlib
import json
import re
import tkinter.messagebox as messagebox


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

def password_vailidity_check(password_input):
    if not re.fullmatch(r"^.{8,}$", password_input):
        messagebox.showerror("Error", "Password must contain at least 8 characters.")
        return False
    # Password must contain at least one capital letters.
    if not re.fullmatch(r".*[A-Z].*", password_input):
        messagebox.showerror("Error", "Password must contain at least one capital letters.")
        return False
    # Password must contain at least one lowercase letters.
    if not re.fullmatch(r".*[a-z].*", password_input):
        messagebox.showerror("Error", "Password must contain at least one lowercase letters.")
        return False
    # Password must contain at least one digit.
    if not re.fullmatch(r".*\d.*", password_input):
        messagebox.showerror("Error", "Password must contain at least one digit.")
        return False
    # Password must contain at least one special character.
    if not re.fullmatch(r"(?=.*[!#$%&'()*+,./:;<=>?@\[\]^_`{|}~]).+", password_input):
        messagebox.showerror("Error", "Password must contain at least one special character.")
        return False
        
    return True