import tkinter as tk
from tkinter import *
import tkinter.font as tkFont
import backend.create_bank_account as create_bank_account
import pages.landing_page as landing_page


#Creates and displays a label, a entry box for account name, a radio button menu for account types and a button.
def display_create_bank_account(user_id):

    #Label and entry box
    global account_name

    account_name_label = tk.Label(create_bank_account_window, text="Account Name:", bg="#B6B6B6")
    account_name_label.grid(column=0, row=1, padx=10, pady=10, sticky="e")

    account_name = tk.Entry(create_bank_account_window)
    account_name.grid(column=1, row=1, padx=10, pady=10, sticky="w")


    account_types = [
        "SAV (Savings Account)", 
        "ISK (Investments Savings Account)", 
        "CHK (Check Account)", 
        "CAS (Casino Account)"]
    
    global account_type
    account_type = StringVar(create_bank_account_window, "CAS (Casino Account)")

    #Radio button menu
    curr_row = 2
    for lang in account_types:
        curr_row += 1
        curr = Radiobutton(create_bank_account_window, text=lang, variable=account_type, value=lang, bg="#B6B6B6")
        curr.grid(column=1, row=curr_row, padx=1, pady=1, sticky="w")

    #"Create new bank account" buttom
    create_button = tk.Button(create_bank_account_window, text="Create New Bank Account", command=lambda: run_create_new_account(user_id))
    create_button.grid(column=1, row=7, pady=10, sticky="w")

#Calls the function that creates and stores a new bank account in data/bank_accounts/accounts.json
#Need the run_create_new_account() to be able to pass parameters to create_new_account()
def run_create_new_account(user_id):
    chosen_type = account_type.get()
    chosen_name = account_name.get()
    try:
        create_bank_account.create_new_account(chosen_type[:3] , chosen_name)
        create_bank_account_window.destroy()
       

        landing_page.display_specific_account(account_id)
    except KeyError:
        print("KeyError in create_new_account")
        print(chosen_type[:3])
        print(chosen_name)

def load_window(parent, user_id):
    global curr_user_id
    curr_user_id = user_id
    global create_bank_account_window
    create_bank_account_window = tk.Toplevel(parent)  # Creates the window
    create_bank_account_window.title('Bankino')
    create_bank_account_window.geometry('600x400')
    create_bank_account_window.configure(bg="#B6B6B6") #Configures background

    #Configures the amount of columns and rows
    ROWS = 20
    COLUMNS = 20
    for i in range(COLUMNS):
        create_bank_account_window.columnconfigure(i, weight=1)
    for i in range(ROWS):
        create_bank_account_window.rowconfigure(i, weight=1)

    
    header_font = tkFont.Font(family="Times", size=25, weight="bold")

    #Creates and display the header
    header = tk.Label(create_bank_account_window, text="Bankino", bg="#B6B6B6", font=header_font)
    header.grid(column=1, row=0, sticky="w", pady=10)
    #Calls the rest of whats to display
    display_create_bank_account(user_id)
