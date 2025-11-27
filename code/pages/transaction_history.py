import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk
import json


# Fetches all account data based on user_id
def get_all_account_data(user_id):
    try: 
        with open ("./data/bank_accounts/accounts.json", "r") as file: 
            accounts = json.load(file)
    except FileNotFoundError:
            print("Error: Accounts database file not found.")

    user_data = accounts[user_id]
    return user_data

# Fetches all the transactions of a specific account
def get_transactions(user_id, account_id):
    all_accounts = get_all_account_data(user_id)
    transaction_history = all_accounts[account_id]['transactions']

    return transaction_history

# Takes the user_id and account_id to create labels for all transactions
def show_transactions(user_id, account_id):
    transaction_history = get_transactions(user_id, account_id)
    
    ammount_labels = []
    date_labels = []
    to_and_from_labels = []

    account_counter = 0
    current_row = 3

    title = tk.Label(transactions, text = f"Transaction History for Account {account_id}", font = header_font)
    title.grid (column = 0, row = 1, sticky='w')

    for transaction in transaction_history:
        ammount_labels.append(tk.Label(transactions, text = f"Amount: {transaction['amount']}", font = header2_font, anchor = "w"))
        ammount_labels[account_counter].grid(column = 0, row = current_row, sticky = "w")

        date_labels.append(tk.Label(transactions, text = f"Date: {transaction['date']}", font = header3_font, anchor = "w"))
        date_labels[account_counter].grid(column = 0, row = current_row + 1, sticky = "w")

        to_and_from_labels.append(tk.Label(transactions, text = f"Transferred from account {transaction["from_acc"]} to account {transaction["to_acc"]}", font = header3_font, anchor = "w"))
        to_and_from_labels[account_counter].grid(column = 0, row = current_row + 2, sticky = "w")

        separator = ttk.Separator(transactions, orient = "horizontal")
        separator.grid(column=0, row=current_row + 3, sticky="we")

        current_row += 4
        account_counter += 1

# Window for displaying the transaction information
def load_window(user_id, account_id):
    global transactions
    transactions = tk.Tk()
    transactions.title(f"Account: {account_id}")
    transactions.geometry('1000x1000')

    # Configures the amount of columns and rows
    ROWS = 20
    COLUMNS = 20
    for i in range(COLUMNS):
        transactions.columnconfigure(i, weight = 1)
    for i in range(ROWS):
        transactions.rowconfigure(i, weight = 1)

    # Different fonts/formatting for labels
    global header2_font
    global header_font
    global value_font
    global header3_font

    header_font = tkFont.Font(family = "Calibri", size = 30, weight = "bold")
    header2_font = tkFont.Font(family = "Calibri", size = 20, weight = "bold")
    value_font = tkFont.Font(family = "Courier", size = 30, weight = "normal")
    header3_font = tkFont.Font(family = "Calibri", size = 20, weight = "normal")

    header = tk.Label(transactions, text = "Bankino", font = header_font)
    header.grid(column = 0, row = 0, sticky = tk.NSEW)
    separator = ttk.Separator(transactions, orient = "horizontal")
    separator.place(relx=0, rely=0.1, relwidth=1, relheight=0)

    show_transactions(user_id, account_id)
    transactions.mainloop()