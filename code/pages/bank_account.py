import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk
import json

# Take the user ID to access their data in the bank_accounts JSON DB.

# hardcoded inputs for now
user_id = "A7P91"
account_id = "CHK12AB"

# Fetches all account data based on user_id
def get_all_account_data(user_id):
    with open ("./data/bank_accounts/accounts.json", "r") as file: 
        accounts = json.load(file)

        user_data = accounts[user_id]
        print(user_data)
        return user_data


# Then take a Bank ID to access the specific bank account details. 
def show_account_data(user_id, account_id):
    all_accounts = get_all_account_data(user_id)

    account_data = all_accounts[account_id]
    account_balance = tk.Label(bank_account, text = (f"Balance: "), font = label_font, anchor = "w")
    account_balance.grid(column = 0, row = 3, sticky = 'w')

    account_balance_value = tk.Label(bank_account, text = (f"{account_data['balance']} {account_data['currency']}"), font = value_font, anchor = "w")
    account_balance_value.grid(column = 0, row = 4, sticky = 'w')

    account_name = tk.Label(bank_account, text = (f"Account Name: {account_data['account_name']}"), font = label_font, anchor = "w")
    account_name.grid(column = 0, row = 6, sticky = 'w')

    account_type = tk.Label(bank_account, text = (f"Account Type: {account_data['account_type']}"), font = label_font, anchor = "w")
    account_type.grid(column = 0, row = 7, sticky = 'w')

    account_currency = tk.Label(bank_account, text = (f"Currency: {account_data['currency']}"), font = label_font, anchor = "w")
    account_currency.grid(column = 0, row = 8, sticky = 'w')


# display the banks details on the screen. 
def main(user_id, account_id):
    global bank_account
    bank_account = tk.Tk()
    bank_account.title(f"Account: {account_id}")
    bank_account.geometry('1000x1000')

    ROWS = 20
    COLUMNS = 20
    for i in range(COLUMNS):
        bank_account.columnconfigure(i, weight = 1)
    for i in range(ROWS):
        bank_account.rowconfigure(i, weight = 1)

    global label_font
    global header_font
    global account_font
    global value_font

    label_font = tkFont.Font(family="Calibri", size = 20, weight = "bold")
    header_font = tkFont.Font(family = "Calibri", size = 30, weight = "bold")
    account_font = tkFont.Font(family="Calibri", size = 25, weight = "normal")
    value_font = tkFont.Font(family = "Courier", size = 30, weight = "normal")

    header = tk.Label(bank_account, text = "Bankino", font = header_font)
    header.grid(column = 0, row = 0, sticky = tk.NSEW)
    title = tk.Label(bank_account, text = f"Account: {account_id}", font = account_font)
    title.grid (column = 0, row = 1)
    separator = ttk.Separator(bank_account, orient = "horizontal")
    separator.place(relx=0, rely=0.1, relwidth=1, relheight=0)

    show_account_data(user_id, account_id)
    bank_account.mainloop()



main(user_id, account_id)