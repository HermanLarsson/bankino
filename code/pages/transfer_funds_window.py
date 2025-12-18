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

        # Window setup
        self.title("Bankino")
        self.geometry("600x600")
        self.configure(bg="#F5F5F0")
        self.resizable(width=False, height=False)

        # GUI setup
        self.create_nav_bar()
        self.grid_layout()
        self.create_header()
        self.display_transfer_funds()


    def create_nav_bar(self):
        nav_bar = tk.Frame(self, bg="#5D866C", width=1000, height=124)
        nav_bar.place(x=0, y=0)

    def grid_layout(self):
    # Configures the amount of columns and rows
        ROWS = 20
        COLUMNS = 20

        for i in range(COLUMNS):
            self.columnconfigure(i, weight=1)
        for i in range(ROWS):
            self.rowconfigure(i, weight=1)

    def create_header(self):
        # Creates the header
        header = tk.Label(self, text="Bankino", font=fonts.header_font, fg="#F5F5F0", bg="#5D866C")
        header.place(x=20, y=16)

    def display_transfer_funds(self):
        # Displays all labels
        from_label = tk.Label(self, text="Choose account to transfer from:", font=fonts.body_font, bg="#F5F5F0", fg="#333333")
        from_label.grid(column=0, row=3, padx=10, pady=10, sticky="e")

        accounts = db_queries.get_bank_accounts_by_user(self.user_id)
        self.from_account = tk.StringVar(self)

        current_row = 3
        
        for acc_id, acc_data in accounts.items():
            current_row += 1
            radiobutton = tk.Radiobutton(self, text=f"{acc_id} ({acc_data['account_name']})", variable=self.from_account, value=acc_id, font=fonts.body_font, bg="#F5F5F0", fg="#333333")
            radiobutton.grid(column=1, row=current_row, sticky="w")

        to_label = tk.Label(self, text="Transfer to (account id):", font=fonts.body_font, bg="#F5F5F0", fg="#333333")
        to_label.grid(column=0, row=current_row + 1, padx=10, pady=10, sticky="e")

        self.to_account_entry = tk.Entry(self)
        self.to_account_entry.grid(column=1, row=current_row + 1, sticky="w")

        amount_label = tk.Label(self, text="Amount:", font=fonts.body_font, bg="#F5F5F0", fg="#333333")
        amount_label.grid(column=0, row=current_row + 2, padx=10, pady=10, sticky="e")

        self.amount_entry = tk.Entry(self)
        self.amount_entry.grid(column=1, row=current_row + 2, sticky="w")

        confirm_button = tk.Button(self, text="Confirm", font=fonts.button_font, bg="#F5F5F0", fg="#333333", bd=0, highlightbackground="#F5F5F0", command=self.process_transfer)
        confirm_button.grid(column=1, row=current_row + 4, pady=20, sticky="w")

    def process_transfer(self):
    # Validates and processes the transfer
        from_acc = self.from_account.get()
        to_acc = self.to_account_entry.get()
        amount_input = self.amount_entry.get()

        user_accounts = db_queries.get_bank_accounts_by_user(self.user_id)

        if from_acc == "":
            messagebox.showinfo("Error", "Select an account to transfer from")
            return

        if user_accounts[from_acc]["is_locked"]:
            answer = messagebox.askquestion(
                "Locked Account",
                f"""Account {from_acc} is locked.

Continuing with this transfer will incur a 100 SEK fine.

Would you like to continue?"""
            )
            if answer == "no":
                return
            db_queries.fine_user(self.user_id, from_acc)

        if to_acc == "":
            messagebox.showinfo("Error", "Select an account to transfer to")
            return

        if not db_queries.check_account_exists(to_acc):
            messagebox.showinfo("Error", f"Account '{to_acc}' does not exist")
            return

        if to_acc == from_acc:
            messagebox.showinfo("Error", "Can't transfer to the same account")
            return

        valid_amount = r"\d+([.,]\d{2})?"
        if not re.fullmatch(valid_amount, amount_input):
            messagebox.showinfo("Error", "Input must be positive and have 0 or 2 decimals")
            return

        amount_value = float(amount_input.replace(",", "."))
        if amount_value == 0:
            messagebox.showinfo("Error", "Amount cannot be 0.00 SEK")
            return

        balance = user_accounts[from_acc]["balance"]
        if not transfer_funds.check_sufficient_funds(balance, amount_value):
            messagebox.showinfo("Error", "Insufficient funds")
            return

        transfer_funds.transfer_money(self.user_id, from_acc, to_acc, amount_value)

        messagebox.showinfo(
            "Success",
            f"{amount_value:.2f} SEK transferred from {from_acc} to {to_acc}"
        )
        self.destroy()
