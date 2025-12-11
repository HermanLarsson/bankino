import tkinter as tk
from tkinter import messagebox
import tkinter.font as tkFont
import backend.password_checker as password_checker
import backend.db_queries as db_queries

#Gets all the information from
def update_account_info(user_id, first_name, middle_name, last_name, phone, email, address, curr_pass, new_pass, confirm_pass):
    
    new_info = {}
    new_info['first_name'] = first_name
    new_info['middle_name'] = middle_name
    new_info['last_name'] = last_name
    new_info['phone'] = phone
    new_info['email'] = email
    new_info['address'] = address
    #new_info['curr_pass'] = password_checker.hash_password(curr_pass)
    new_info['password'] = password_checker.hash_password(new_pass)
    #new_info['confirm_pass'] = password_checker.hash_password(confirm_pass)

    curr_pass = password_checker.hash_password(curr_pass)
    confirm_pass = password_checker.hash_password(confirm_pass)

    current_user_info = db_queries.get_user_info(user_id)

    errors = []
    error_message = ""
    
    if db_queries.verify_user(current_user_info['personal_number'], curr_pass) == user_id:
        if new_info['first_name'] == '':
            errors.append("You must have a first name!")
        if new_info['last_name'] == '':
            errors.append("You must have a last name!")
        if new_info['password'] != confirm_pass:
            errors.append("Passwords don't match!")
    else:
        errors.append("You have entered an incorrect password!")

    if len(errors) > 0:
        for error in errors:
            error_message += (error + '\n')
        messagebox.showerror("Error", error_message)
        return False
    else:
        if db_queries.update_user_info(user_id, new_info):
            messagebox.showinfo("Success!", "Your account has been updated!")
            return True
        else:
            messagebox.showerror("Error", "An error occured while saving the account information. Please panic.")
            return False


def display_account_management(user_id):
    # loads the user data from database
    user_data = db_queries.get_user_info(user_id)

    # first name 
    first_name_label = tk.Label(account_management_window, text="First Name:", bg="#B6B6B6")
    first_name_label.grid(column=0, row=1, padx=10, pady=10, sticky="e")
    first_name_entry = tk.Entry(account_management_window)
    first_name_entry.grid(column=1, row=1, padx=10, pady=10, sticky="w")
    
    # middle name 
    middle_name_label = tk.Label(account_management_window, text="Middle Name:", bg="#B6B6B6")
    middle_name_label.grid(column=0, row=2, padx=10, pady=10, sticky="e")
    middle_name_entry = tk.Entry(account_management_window)
    middle_name_entry.grid(column=1, row=2, padx=10, pady=10, sticky="w")
    
    # last name
    last_name_label = tk.Label(account_management_window, text="Last Name:", bg="#B6B6B6")
    last_name_label.grid(column=0, row=3, padx=10, pady=10, sticky="e")
    last_name_entry = tk.Entry(account_management_window)
    last_name_entry.grid(column=1, row=3, padx=10, pady=10, sticky="w")
    
    # phone number
    phone_label = tk.Label(account_management_window, text="Phone Number:", bg="#B6B6B6")
    phone_label.grid(column=0, row=4, padx=10, pady=10, sticky="e")
    phone_entry = tk.Entry(account_management_window)
    phone_entry.grid(column=1, row=4, padx=10, pady=10, sticky="w")
    
    # email
    email_label = tk.Label(account_management_window, text="Email:", bg="#B6B6B6")
    email_label.grid(column=0, row=5, padx=10, pady=10, sticky="e")
    email_entry = tk.Entry(account_management_window)
    email_entry.grid(column=1, row=5, padx=10, pady=10, sticky="w")
    
    # address
    address_label = tk.Label(account_management_window, text="Address:", bg="#B6B6B6")
    address_label.grid(column=0, row=6, padx=10, pady=10, sticky="e")
    address_entry = tk.Entry(account_management_window)
    address_entry.grid(column=1, row=6, padx=10, pady=10, sticky="w")
   

    # current password 
    current_password_label = tk.Label(account_management_window, text="Current Password:", bg="#B6B6B6")
    current_password_label.grid(column=0, row=7, padx=10, pady=10, sticky="e")
    current_password_entry = tk.Entry(account_management_window, show="*")
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

    # inserts for the fields from the database
    first_name_entry.insert(0, user_data["first_name"])  
    middle_name_entry.insert(0, user_data["middle_name"])
    last_name_entry.insert(0, user_data["last_name"]) 

     # inserts phone if it is in database else empty string
    if "phone" in user_data:
        phone_entry.insert(0, user_data["phone"])
    else:
        phone_entry.insert(0, "")

     # inserts email if it is in database else empty string
    if "email" in user_data:
        email_entry.insert(0, user_data["email"])
    else:
        email_entry.insert(0, "")

    # inserts address if it is in database else empty string
    if "address" in user_data:
        address_entry.insert(0, user_data["address"])
    else:
        address_entry.insert(0, "")

    # save button 
    save_button = tk.Button(account_management_window, text="Save", command=lambda: update_account_info(user_id, first_name_entry.get(), middle_name_entry.get(), last_name_entry.get(), phone_entry.get(), email_entry.get(), address_entry.get(), current_password_entry.get(), new_password_entry.get(), confirm_password_entry.get()))
    save_button.grid(column=1, row=10, pady=20, sticky="w")

def load_window(parent, user_id):
    global account_management_window

    account_management_window = tk.Toplevel(parent)
    account_management_window.title("Account Management")
    account_management_window.geometry("600x600")
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

    display_account_management(user_id)



    

     


    









    


    


    