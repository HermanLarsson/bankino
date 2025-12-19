import backend.db_queries as db_queries
import tkinter as tk
import re
import fonts.bankino_fonts as fonts

class DepositFundsWindow(tk.Toplevel):

    def __init__(self, parent, user_id):
        super().__init__(parent)

        self.user_id = user_id
        self.avail_accounts = db_queries.get_bank_accounts_by_user(user_id)

        # Window setup
        self.title("Bankino")
        self.geometry("600x400")

        # GUI setup
        ROWS = 20
        COLUMNS = 20
        for i in range(COLUMNS):
            self.columnconfigure(i, weight=1)
        for i in range(ROWS):
            self.rowconfigure(i, weight=1)

        # Header 
        window_label = tk.Label(self, text="Deposit Funds", font=fonts.header2_font)
        window_label.grid(column=0, row=1, padx=10, pady=10, sticky="e")

        amount_label = tk.Label(self, text="Amount:")
        amount_label.grid(column=0, row=4, padx=10, pady=10, sticky="e")

        self.amount_entry = tk.Entry(self)
        self.amount_entry.grid(column=1, row=4, padx=10, pady=10, sticky="w")

        # Selection of account 
        self.create_account_choices()
        
        # Confirm button
        confirm_button = tk.Button(self, text="Deposit", command=self.process_deposit)
        confirm_button.grid(column=5, row=10, sticky="S")

   
    def create_account_choices(self):
        account_buttons = []
        account_counter = 0
        current_row = 6

        # Saves the account the user selected
        self.account_choice = tk.StringVar(self, next(iter(self.avail_accounts)))

       # Loops through the users' accounts and creates the radiobutton the user can select which account to transfer from
        for account in self.avail_accounts.items():
            account_buttons.append(
                tk.Radiobutton(self, text=account[0] + " - " + account[1]["account_name"], value=account[0], variable=self.account_choice))
            
            account_buttons[account_counter].grid(column=0, row=current_row)
            current_row += 1
            account_counter += 1

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
