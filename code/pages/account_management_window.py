import tkinter as tk
from tkinter import messagebox
import tkinter.font as tkFont

account_management_window = None 

def display_account_management():
    global first_name_entry, last_name_entry, middle_name_entry
    global phone_entry, email_entry, address_entry
    global current_password_entry, new_password_entry

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

    # email
    address_label = tk.Label(account_management_window, text="Address:", bg="#B6B6B6")
    address_label.grid(column=0, row=6, padx=10, pady=10, sticky="e")
    address_entry = tk.Entry(account_management_window)
    address_entry.grid(column=1, row=6, padx=10, pady=10, sticky="w")

    # current password 
    current_password_label = tk.Label(account_management_window, text="Current Password:", bg="#B6B6B6")
    current_password_label.grid(column=0, row=7, padx=10, pady=10, sticky="e")
    current_password_entry = tk.Entry(account_management_window)
    current_password_entry.grid(column=1, row=7, padx=10, pady=10, sticky="w")

    # new password 
    new_password_label = tk.Label(account_management_window, text="New Password:", bg="#B6B6B6")
    new_password_label.grid(column=0, row=8, padx=10, pady=10, sticky="e")
    new_password_entry = tk.Entry(account_management_window)
    new_password_entry.grid(column=1, row=8, padx=10, pady=10, sticky="w")

    # save button 
    save_button = tk.Button(account_management_window, text="Save", command=lambda: print("Logic here"))
    save_button.grid(column=1, row=10, pady=20, sticky="w")

def load_window(parent):
    global account_management_window
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



    

     


    









    


    


    