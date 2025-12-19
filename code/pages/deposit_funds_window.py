import backend.db_queries as db_queries
import tkinter as tk
import fonts.bankino_fonts as tkFont
from tkinter import *
import re

def create_account_choices(avail_accounts):
    account_buttons = []
    #Counter for the loop
    account_counter = 0
    #Starting at row 6 in the layout of the page
    current_row = 11

    global account_choice
    account_choice = StringVar(deposit_funds_window, next(iter(avail_accounts)))

    #Loops through all the user's accounts and adds them to a list of the avail. choices.
    #Then creates a button for the current account and stores the button in the list of buttons
    for account in avail_accounts.items():
        account_buttons.append(tk.Radiobutton(deposit_funds_window, text = account[0] + " - " + account[1]['account_name'], value = account[0], variable = account_choice, bg="#F5F5F0", fg="#333333", font=tkFont.body_font))
        account_buttons[account_counter].grid(column = 0, row = current_row)
        current_row += 1
        account_counter += 1

def process_deposit(user_id, account_id, amount):
    print("Processing")
    valid_input = r'\d+([.,]\d{2})?'
    if re.fullmatch(valid_input, amount):
        try:
            amount = re.sub(r',', r'.', amount)
            amount = float(amount)

            if amount == 0:
                tk.messagebox.showinfo("Error", "Input cannot be 0,00 SEK")
            else:
                db_queries.deposit_funds(user_id, account_id, amount)
                print(f"{amount} succcessfully deposited to account {account_id}")
                tk.messagebox.showinfo("Success", f"{amount:.2f} SEK succcessfully deposited to account {account_id}")
                deposit_funds_window.destroy()
        except TypeError: 
            print("Invalid amount entered!")  
    else:
        print("Amount must be greater than 0")
        tk.messagebox.showinfo("Error", "Input must be positive and have 0 or 2 decimal places")
    
def load_window(parent, user_id):
    avail_accounts = db_queries.get_bank_accounts_by_user(user_id)

    global deposit_funds_window
    # uses Toplevel instead of Tk since it is a 'child' window
    deposit_funds_window = tk.Toplevel(parent) #Creates the window
    deposit_funds_window.title('Bankino')
    deposit_funds_window.geometry('600x600')
    deposit_funds_window.configure(bg="#F5F5F0")
    deposit_funds_window.resizable(width=False, height=False)

    #Configures the amount of columns and rows
    ROWS = 20
    COLUMNS = 20
    for i in range(COLUMNS):
        deposit_funds_window.columnconfigure(i, weight=1)
    for i in range(ROWS):
        deposit_funds_window.rowconfigure(i, weight=1)

   # Nav bar
    nav_bar = tk.Frame(deposit_funds_window, bg="#5D866C", width=600, height=124)
    nav_bar.place(x=0, y=0)

    # Header
    header = tk.Label(deposit_funds_window, text="Deposit Funds", bg="#5D866C", fg="#F5F5F0", font=tkFont.header_font)
    header.place(x=20, y=16)

    amount_label = tk.Label(deposit_funds_window, text="Amount:", bg="#F5F5F0", fg="#333333", font=tkFont.body_font)
    amount_label.grid(column=0, row=10, padx=10, pady=10, sticky="e")

    amount_entry = tk.Entry(deposit_funds_window, font=tkFont.body_font)
    amount_entry.grid(column=1, row=10, padx=10, pady=10, sticky="w")
    
    create_account_choices(avail_accounts)

    confirm_button = tk.Button(deposit_funds_window, text = "Deposit", command=lambda : process_deposit(user_id, account_choice.get(), amount_entry.get()), font=tkFont.button_font, bg="#F5F5F0", fg="#333333", bd=0, highlightbackground="#F5F5F0")
    confirm_button.grid(column=5, row=10, sticky="S")

