import tkinter as tk
from tkinter import ttk
import backend.db_queries as db_queries
import fonts.bankino_fonts as fonts

class TransactionHistory(tk.Toplevel):
    def __init__(self, parent, user_id, account_id):
        super().__init__(parent)

        self.parent = parent 
        self.user_id = user_id 
        self.account_id = account_id

        # Window setup
        self.title(f"Transaction History fot {account_id}")
        self.geometry("1000x1000")

        # When the user closes the page the program terminates
        self.protocol("WM_DELETE_WINDOW", self.go_back)

        # Methods that are called upon instantiation
        self.grid_layout()
        self.create_header()

        # displays transactions
        self.show_transactions()

        # back button
        self.create_back_button()

        # GUI setup
    def grid_layout(self):
        ROWS = 20
        COLUMNS = 20
        for i in range(COLUMNS):
            self.columnconfigure(i, weight = 1)
        for i in range(ROWS):
            self.rowconfigure(i, weight = 1)

    def create_header(self):
        header = tk.Label(self, text="Bankino", font=fonts.header_font)
        header.grid(column=0, row=0, sticky="w", padx=20)

        separator = ttk.Separator(self, orient="horizontal")
        separator.grid(column=0, row=1, columnspan=20, sticky="ew", pady=10)

        title = tk.Label(self, text=f"Transaction History for Account {self.account_id}", font=fonts.header2_font)
        title.grid(column=0, row=2, sticky="w", padx=20)

    def get_transactions(self):
        all_accounts = db_queries.get_bank_accounts_by_user(self.user_id)
        transaction_history = all_accounts[self.account_id]['transactions']
        return transaction_history

        # creates labels for transactions
    def show_transactions(self):
        transaction_history = self.get_transactions()
        current_row = 4

        for transaction in transaction_history:
            amount_label = tk.Label(self, text=f"Amount: {transaction['amount']}", font=fonts.body_font, anchor="w")
            amount_label.grid(column=0, row=current_row, sticky="w", padx=20)

            date_label = tk.Label(self, text=f"Date: {transaction['date']}", font=fonts.body_font, anchor="w")
            date_label.grid(column=0, row=current_row + 1, sticky="w", padx=20)

            transfer_label = tk.Label(self, text=f"Transferred from account {transaction['from_acc']} to account {transaction['to_acc']}", font=fonts.body_font, anchor="w")
            transfer_label.grid(column=0, row=current_row + 2, sticky="w", padx=20)

            separator = ttk.Separator(self, orient="horizontal")
            separator.grid(column=0, row= current_row + 3, columnspan=20, sticky="ew",pady=10)

            current_row += 4

    def create_back_button(self):
        back_button = tk.Button(self, text="Back to Account", font=fonts.button_font, command=self.go_back)
        back_button.grid(column=0, row=19, sticky="W", padx=20, pady=20)

    def go_back(self):
        self.destroy()
        self.parent.deiconify()
            
                                    
    
   