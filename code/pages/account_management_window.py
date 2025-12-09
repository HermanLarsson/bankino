import tkinter as tk
from tkinter import messagebox
import tkinter.font as tkFont
import backend.db_queries as db_queries

account_management_window = None 
current_user_id = None

def display_account_management():
    global first_name_entry, last_name_entry, middle_name_entry
    global phone_entry, email_entry, address_entry
    global current_password_entry, new_password_entry, confirm_password_entry

    # loads the user data from database
    user_data = db_queries.get_user_info(current_user_id)

    # first name 
    first_name_label = tk.Label(account_management_window, text="First Name:", bg="#B6B6B6")
    first_name_label.grid(column=0, row=1, padx=10, pady=10, sticky="e")
    first_name_entry = tk.Entry(account_management_window)
    first_name_entry.grid(column=1, row=1, padx=10, pady=10, sticky="w")
    first_name_entry.insert(0, user_data["first_name"]) # inserts the first name from the database 

    # middle name 
    middle_name_label = tk.Label(account_management_window, text="Middle Name:", bg="#B6B6B6")
    middle_name_label.grid(column=0, row=2, padx=10, pady=10, sticky="e")
    middle_name_entry = tk.Entry(account_management_window)
    middle_name_entry.grid(column=1, row=2, padx=10, pady=10, sticky="w")
    middle_name_entry.insert(0, user_data["middle_name"]) # inserts the middle name from databse

    # last name
    last_name_label = tk.Label(account_management_window, text="Last Name:", bg="#B6B6B6")
    last_name_label.grid(column=0, row=3, padx=10, pady=10, sticky="e")
    last_name_entry = tk.Entry(account_management_window)
    last_name_entry.grid(column=1, row=3, padx=10, pady=10, sticky="w")
    last_name_entry.insert(0, user_data["last_name"]) # inserts the last name from database

    # phone number
    phone_label = tk.Label(account_management_window, text="Phone Number:", bg="#B6B6B6")
    phone_label.grid(column=0, row=4, padx=10, pady=10, sticky="e")
    phone_entry = tk.Entry(account_management_window)
    phone_entry.grid(column=1, row=4, padx=10, pady=10, sticky="w")
    
    # inserts phone if it is in database else empty string
    if "phone" in user_data:
        phone_entry.insert(0, user_data["phone"])
    else:
        phone_entry.insert(0, "")

    # email
    email_label = tk.Label(account_management_window, text="Email:", bg="#B6B6B6")
    email_label.grid(column=0, row=5, padx=10, pady=10, sticky="e")
    email_entry = tk.Entry(account_management_window)
    email_entry.grid(column=1, row=5, padx=10, pady=10, sticky="w")
    
    # inserts email if it is in database else empty string
    if "email" in user_data:
        email_entry.insert(0, user_data["email"])
    else:
        email_entry.insert(0, "")

    # address
    address_label = tk.Label(account_management_window, text="Address:", bg="#B6B6B6")
    address_label.grid(column=0, row=6, padx=10, pady=10, sticky="e")
    address_entry = tk.Entry(account_management_window)
    address_entry.grid(column=1, row=6, padx=10, pady=10, sticky="w")
   
   # inserts address if it is in database else empty string
    if "address" in user_data:
        address_entry.insert(0, user_data["address"])
    else:
        address_entry.insert(0, "")

    # current password 
    current_password_label = tk.Label(account_management_window, text="Current Password:", bg="#B6B6B6")
    current_password_label.grid(column=0, row=7, padx=10, pady=10, sticky="e")
    current_password_entry = tk.Entry(account_management_window,show="*")
    current_password_entry.grid(column=1, row=7, padx=10, pady=10, sticky="w")
   
    # new password 
    new_password_label = tk.Label(account_management_window, text="New Password:", bg="#B6B6B6")
    new_password_label.grid(column=0, row=8, padx=10, pady=10, sticky="e")
    new_password_entry = tk.Entry(account_management_window, show="*")
    new_password_entry.grid(column=1, row=8, padx=10, pady=10, sticky="w")

    # confirm new password
    confirm_password_label = tk.Label(account_management_window, text="Confirm Password:", bg="#B6B6B6")
    confirm_password_label.grid(column=0, row=9, padx=10, pady=10, sticky="e")
    confirm_password_entry = tk.Entry(account_management_window, show="*")
    confirm_password_entry.grid(column=1, row=9, padx=10, pady=10, sticky="w")

    
    # save button 
    save_button = tk.Button(account_management_window, text="Save", command=lambda: print("Logic here"))
    save_button.grid(column=1, row=10, pady=20, sticky="w")

def load_window(parent, user_id):
    global account_management_window
    global current_user_id
    current_user_id = user_id

    account_management_window = tk.Toplevel(parent)
    account_management_window.title("Account Management")
    account_management_window.geometry("600x500")
    account_management_window.configure(bg="#B6B6B6")

    # configure the grid
    ROWS = 15
    COLUMNS = 3
    for i in range(COLUMNS):
        account_management_window.columnconfigure(i, weight=1)
    for i in range(ROWS):
        account_management_window.rowconfigure(i, weight=1)

    # Header
    header_font = tkFont.Font(family="Times", size=25, weight="bold")
    header = tk.Label(account_management_window, text="Bankino", bg="#B6B6B6", font=header_font)
    header.grid(column=1, row=0, sticky="w", pady=10)

    display_account_management()



    

     


    









    


    


    