import tkinter as tk
from tkinter import messagebox
import re

import backend.db_queries as db_queries
import backend.logic_for_transfer_funds as transfer_funds
import fonts.bankino_fonts as fonts


class TransferFundsWindow(tk.Toplevel):

    def __init__(self, parent, user_id):
        super().__init__(parent)

        self.user_id = user_id

        # window setup
        self.title("Bankino - Transfer Funds")
        self.geometry("600x400")
        self.configure(bg="#B6B6B6")

        # GUI setup
        ROWS = 20
        COLUMNS = 20
        for i in range(COLUMNS):
            self.columnconfigure(i, weight=1)
        for i in range(ROWS):
            self.rowconfigure(i, weight=1)

        # Header 
        header = tk.Label(self, text="Bankino", bg="#B6B6B6", font=fonts.header_font)
        header.grid(column=1, row=0, sticky="w", pady=10)
       
        self.display_transfer_funds()


    def display_transfer_funds(self):

       
        from_label = tk.Label(self, text="Choose account to transfer from:", bg="#B6B6B6")
        from_label.grid(column=0, row=1, padx=10, pady=10, sticky="e")

        # Get the user bank accounts
        accounts = db_queries.get_bank_accounts_by_user(self.user_id)

        # Store the account the user transfers from
        self.from_account = tk.StringVar(self)

        curr_row = 1
        for acc_id, acc_data in accounts.items():
            curr_row += 1
            radiobutton = tk.Radiobutton(self, text=f"{acc_id} ({acc_data['account_name']})", variable=self.from_account, value=acc_id, bg="#B6B6B6")
            radiobutton.grid(column=1, row=curr_row, padx=1, pady=1, sticky="w")

        # To account label
        to_label = tk.Label(self, text="Transfer to (account id):", bg="#B6B6B6")
        to_label.grid(column=0, row=curr_row + 2, padx=10, pady=10, sticky="e")

        self.to_account = tk.Entry(self)
        self.to_account.grid(column=1, row=curr_row + 2, padx=10, pady=10, sticky="w")

        # Amount label
        amount_label = tk.Label(self, text="Amount:", bg="#B6B6B6")
        amount_label.grid(column=0, row=curr_row + 3, padx=10, pady=10, sticky="e")

        self.amount = tk.Entry(self)
        self.amount.grid(column=1, row=curr_row + 3, padx=10, pady=10, sticky="w")

        # Confirm button
        confirm_button = tk.Button(self, text="Confirm", command=self.process_transfer)
        confirm_button.grid(column=1, row=curr_row + 5, pady=10, sticky="w")


    def process_transfer(self):
        print("Processing")

        # Varibles to save user input
        from_acc_input = self.from_account.get()
        to_acc_input = self.to_account.get()
        amount_input = self.amount.get()

        user_accounts = db_queries.get_bank_accounts_by_user(self.user_id)

        if user_accounts[from_acc_input]['is_locked']:
            answer = messagebox.askquestion("Locked Account", 
            f"""Account {from_acc_input} is locked.

            Continuing with this transfer will incur a 100 SEK fine.

            Would you like to continue with the transfer?"""
        )

            if answer == "no":
                return
            else:
                db_queries.fine_user(self.user_id, from_acc_input)

        if from_acc_input == "":
            messagebox.showinfo("Error", "Select an account to transfer from")
            return

        if to_acc_input == "":
            messagebox.showinfo("Error", "Select an account to transfer to")
            return

        if amount_input == "":
            messagebox.showinfo("Error", "Select an amount to transfer")
            return

        if not db_queries.check_account_exists(to_acc_input):
            messagebox.showinfo("Error", f"Account '{to_acc_input}' does not exist")
            return

        if to_acc_input == from_acc_input:
            messagebox.showinfo("Error", "Can't transfer to the same account")
            return

        valid_input = r'\d+([.,]\d{2})?'
        if re.fullmatch(valid_input, amount_input):
            try:
                amount_input = amount_input.replace(",", ".")
                amount_value = float(amount_input)

                if amount_value == 0:
                    messagebox.showinfo("Error", "Input cannot be 0.00 SEK")
                    return

                current_balance = user_accounts[from_acc_input]['balance']
                if not transfer_funds.check_sufficient_funds(current_balance, amount_value):
                    messagebox.showinfo(
                        "Error",
                        f"Account {from_acc_input} does not have sufficient funds"
                    )
                    return

                transfer_funds.transfer_money(self.user_id, from_acc_input, to_acc_input, amount_value)

                messagebox.showinfo("Success", f"{amount_value:.2f} SEK successfully transferred from "f"{from_acc_input} to {to_acc_input}")
                self.destroy()

            except ValueError:
                messagebox.showinfo("Error", "Invalid amount entered")
        else:
            messagebox.showinfo("Error", "Input must be positive and have 0 or 2 decimal places")

