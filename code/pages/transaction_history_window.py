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
                # Window setup
        self.title(f"Transaction History for {account_id}")
        self.geometry("600x600")
        self.configure(bg="#F5F5F0")
        self.resizable(width=False, height=False)

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
        nav_bar = tk.Frame(self, bg="#5D866C", width=600, height=124)
        nav_bar.place(x=0, y=0)

        header = tk.Label(self, text="Bankino", font=fonts.header_font, bg="#5D866C", fg="#F5F5F0")
        header.place(x=20, y=16)

        title = tk.Label(self, text=f"Transaction History for Account {self.account_id}", font=fonts.header2_font, bg="#F5F5F0", fg="#333333")
        title.place(x=20, y=210)

        separator = ttk.Separator(self, orient="horizontal")
        separator.place(x=0, y=260, width=600)

    def get_transactions(self):
        all_accounts = db_queries.get_bank_accounts_by_user(self.user_id)
        transaction_history = all_accounts[self.account_id]['transactions']
        return transaction_history

        # creates labels for transactions
    def show_transactions(self):
        transaction_history = self.get_transactions()
        current_y = 280  # Start below the separator
        
        for transaction in transaction_history:
            amount_label = tk.Label(self, text=f"Amount: {transaction['amount']}", font=fonts.body_font, anchor="w", bg="#F5F5F0", fg="#333333")
            amount_label.place(x=20, y=current_y)
            
            date_label = tk.Label(self, text=f"Date: {transaction['date']}", font=fonts.body_font, anchor="w", bg="#F5F5F0", fg="#333333")
            date_label.place(x=20, y=current_y + 30)
            
            transfer_label = tk.Label(self, text=f"Transferred from account {transaction['from_acc']} to account {transaction['to_acc']}", font=fonts.body_font, anchor="w", bg="#F5F5F0", fg="#333333")
            transfer_label.place(x=20, y=current_y + 60)
            
            separator = tk.Frame(self, bg="#CCCCCC", height=1)
            separator.place(x=20, y=current_y + 95, width=560)
            
            current_y += 110

    def create_back_button(self):
        back_button = tk.Button(self, text="Back to Account", font=fonts.button_font, bg="#F5F5F0", fg="#333333", bd=0, highlightbackground="#F5F5F0", command=self.go_back)
        back_button.place(x=20, y=560)

    def go_back(self):
        self.destroy()
        self.parent.deiconify()
            
                                    
    
   