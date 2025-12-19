import backend.db_queries as db_queries
import tkinter as tk
import fonts.bankino_fonts as tkFont
from tkinter import *
import re

class DepositFundsWindow(tk.Toplevel):

    def __init__(self, parent, user_id):
        super().__init__(parent)

        self.user_id = user_id
        self.avail_accounts = db_queries.get_bank_accounts_by_user(user_id)

        # Window setup
        self.geometry('600x600')
        self.configure(bg="#F5F5F0")
        self.resizable(width=False, height=False)

        # GUI setup
        ROWS = 20
        COLUMNS = 20
        for i in range(COLUMNS):
            self.columnconfigure(i, weight=1)
        for i in range(ROWS):
            self.rowconfigure(i, weight=1)
        
        # Nav bar
        nav_bar = tk.Frame(self, bg="#5D866C", width=600, height=124)
        nav_bar.place(x=0, y=0)

        # Header 
        window_label = tk.Label(self, text="Deposit Funds", bg="#5D866C", fg="#F5F5F0", font=tkFont.header_font)
        window_label.place(x=20, y=16)

        amount_label = tk.Label(self, text="Amount:", bg="#F5F5F0", fg="#333333", font=tkFont.body_font)
        amount_label.grid(column=0, row=10, padx=10, pady=10, sticky="e")

        self.amount_entry = tk.Entry(self, font=tkFont.body_font)
        self.amount_entry.grid(column=1, row=10, padx=10, pady=10, sticky="w")

        # Selection of account 
        last_row = self.create_account_choices()
        
        # Confirm button
        confirm_button = tk.Button(self, text = "Deposit", command=lambda : self.process_deposit(), font=tkFont.button_font, bg="#F5F5F0", fg="#333333", bd=0, highlightbackground="#F5F5F0")
        confirm_button.grid(column=1, row=last_row + 1, sticky="S")

   
    def create_account_choices(self):
        account_buttons = []
        account_counter = 0
        current_row = 11

        # Saves the account the user selected
        self.account_choice = tk.StringVar(self, next(iter(self.avail_accounts)))

    #Loops through all the user's accounts and adds them to a list of the avail. choices.
    #Then creates a button for the current account and stores the button in the list of buttons
        for account in self.avail_accounts.items():
            account_buttons.append(tk.Radiobutton(self, text = account[0] + " - " + account[1]['account_name'], value = account[0], variable = self.account_choice, bg="#F5F5F0", fg="#333333", font=tkFont.body_font))
            account_buttons[account_counter].grid(column = 1, row = current_row)
            current_row += 1
            account_counter += 1

        return current_row

    # Validation and processing of the deposit
    def process_deposit(self):
        print("Processing")

        amount = self.amount_entry.get()
        account_id = self.account_choice.get()

        valid_input = r"\d+([.,]\d{2})?"
        if re.fullmatch(valid_input, amount):
            try:
                amount = amount.replace(",", ".")
                amount = float(amount)

                if amount == 0:
                    tk.messagebox.showinfo("Error", "Input cannot be 0,00 SEK")
                else:
                    db_queries.deposit_funds(self.user_id, account_id, amount)
                    print(f"{amount} successfully deposited to account {account_id}")
                    tk.messagebox.showinfo("Success", f"{amount:.2f} SEK successfully deposited to account {account_id}")
                    self.destroy()
            except TypeError:
                print("Invalid amount entered!")
        else:
            print("Amount must be greater than 0")
            tk.messagebox.showinfo("Error", "Input must be positive and have 0 or 2 decimal places")
