import backend.db_queries as db_queries
import tkinter as tk
import tkinter.font as tkFont
from tkinter import *



def create_account_choices(avail_accounts):
    account_buttons = []
    #Counter for the loop
    account_counter = 0
    #Starting at row 6 in the layout of the page
    current_row = 6

    global account_choice
    account_choice = StringVar(deposit_funds_window, next(iter(avail_accounts)))

    #Loops through all the user's accounts and adds them to a list of the avail. choices.
    #Then creates a button for the current account and stores the button in the list of buttons
    for account in avail_accounts.items():
        account_buttons.append(tk.Radiobutton(deposit_funds_window, text = account[0] + " - " + account[1]['account_name'], value = account[0], variable = account_choice))
        account_buttons[account_counter].grid(column = 0, row = current_row)
        current_row += 1
        account_counter += 1


def load_window(parent, user_id):
    avail_accounts = db_queries.get_all_account_data(user_id)

    global deposit_funds_window
    # uses Toplevel instead of Tk since it is a 'child' window
    deposit_funds_window = tk.Toplevel(parent) #Creates the window
    deposit_funds_window.title('Bankino')
    deposit_funds_window.geometry('600x400')
       
    #Configures the amount of columns and rows
    ROWS = 20
    COLUMNS = 20
    for i in range(COLUMNS):
        deposit_funds_window.columnconfigure(i, weight=1)
    for i in range(ROWS):
        deposit_funds_window.rowconfigure(i, weight=1)

    global header2_font
    header2_font = tkFont.Font(family="Calibri", size = 25, weight = "bold")

    window_label = tk.Label(deposit_funds_window, text="Deposit Funds")
    window_label.grid(column=0, row=1, padx=10, pady=10, sticky="e")

    amount_label = tk.Label(deposit_funds_window, text="Amount:")
    amount_label.grid(column=0, row=4, padx=10, pady=10, sticky="e")

    amount_entry = tk.Entry(deposit_funds_window)
    amount_entry.grid(column=1, row=4, padx=10, pady=10, sticky="w")
    


    create_account_choices(avail_accounts)

    confirm_button = tk.Button(deposit_funds_window, text = "Deposit", command=lambda: print(account_choice.get(), amount_entry.get()))
    confirm_button.grid(column=5, row=10, sticky="S")

