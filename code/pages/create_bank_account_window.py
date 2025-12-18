import tkinter as tk
from tkinter import *
import fonts.bankino_fonts as tkFont
import backend.create_bank_account as create_bank_account
import pages.landing_page as landing_page


#Creates and displays a label, a entry box for account name, a radio button menu for account types and a button.
def display_create_bank_account():

    #Label and entry box
    global account_name

    account_name_label = tk.Label(create_bank_account_window, text="Account Name:", bg="#F5F5F0", fg="#333333", font=tkFont.body_font)
    account_name_label.grid(column=0, row=10, padx=10, pady=10, sticky="e")

    account_name = tk.Entry(create_bank_account_window, font=tkFont.body_font)
    account_name.grid(column=1, row=10, padx=10, pady=10, sticky="w")


    account_types = [
        "SAV (Savings Account)", 
        "ISK (Investments Savings Account)", 
        "CHK (Check Account)", 
        "CAS (Casino Account)"]
    
    global account_type
    account_type = StringVar(create_bank_account_window, "CAS (Casino Account)")

    #Radio button menu
    curr_row = 11
    for lang in account_types:
        curr_row += 1
        curr = Radiobutton(create_bank_account_window, text=lang, variable=account_type, value=lang, bg="#F5F5F0", fg="#333333", font=tkFont.body_font)
        curr.grid(column=1, row=curr_row, padx=1, pady=1, sticky="w")

    # Initialize needs_card as False by default
    global needs_card
    needs_card = BooleanVar(create_bank_account_window, False)

    # Generate card checkbox
    generate_card_checkbox = tk.Checkbutton(create_bank_account_window, text="Order Card", variable=needs_card, bg="#F5F5F0", fg="#333333", 
                                            font=tkFont.body_font)
    generate_card_checkbox.grid(column=1, row=16, pady=10, sticky="w")

    #"Create new bank account" buttom
    create_button = tk.Button(create_bank_account_window, text="Create New Bank Account", command=run_create_new_account,
                               font=tkFont.button_font, bg="#F5F5F0", fg="#333333", bd=0, highlightbackground="#F5F5F0")
    create_button.grid(column=1, row=17, pady=10, sticky="w")


#Calls the function that creates and stores a new bank account in data/bank_accounts/accounts.json
#Need the run_create_new_account() to be able to pass parameters to create_new_account()
def run_create_new_account():
    chosen_type = account_type.get()
    chosen_name = account_name.get()
    card_needed = needs_card.get()
    try:
        account_id = create_bank_account.create_new_account(chosen_type[:3] , chosen_name , card_needed)
        create_bank_account_window.destroy()
       


    except KeyError:
        print("KeyError in create_new_account")
        print(chosen_type[:3])
        print(chosen_name)
    # TODO: DOUBLE CHECK THIS!
    # landing_page.display_specific_account(account_id)

def load_window(parent, user_id):
    global curr_user_id
    curr_user_id = user_id
    global create_bank_account_window
    create_bank_account_window = tk.Toplevel(parent)  # Creates the window
    create_bank_account_window.title('Bankino')
    create_bank_account_window.geometry('600x600')
    create_bank_account_window.configure(bg="#F5F5F0") #Configures background

    #Configures the amount of columns and rows
    ROWS = 20
    COLUMNS = 20
    for i in range(COLUMNS):
        create_bank_account_window.columnconfigure(i, weight=1)
    for i in range(ROWS):
        create_bank_account_window.rowconfigure(i, weight=1)

    create_bank_account_window.resizable(width=False, height=False)

    # Nav bar
    nav_bar = tk.Frame(create_bank_account_window, bg="#5D866C", width=600, height=124)
    nav_bar.place(x=0, y=0)

    # Header
    header = tk.Label(create_bank_account_window, text="Create Bank Account", bg="#5D866C", fg="#F5F5F0", font=tkFont.header_font)
    header.place(x=20, y=16)
    
    #Calls the rest of whats to display
    display_create_bank_account()
