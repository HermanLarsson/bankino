import tkinter as tk
import fonts.bankino_fonts as fonts
from tkinter import ttk, messagebox
from datetime import datetime, timedelta
import backend.db_queries as db_queries
import fonts.bankino_fonts as fonts


class SavingsWindow(tk.Toplevel):

    def __init__(self, parent, account_id, user_id):
        super().__init__(parent)

        self.account_id = account_id
        self.user_id = user_id

       # window setup
        self.title(f"Account: {account_id}")
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

        # Create Header
        nav_bar = tk.Frame(self, bg="#5D866C", width=600, height=124)
        nav_bar.place(x=0, y=0)

        header = tk.Label(self, text="Bankino", font=fonts.header_font, bg="#5D866C", fg="#F5F5F0")
        header.place(x=20, y=16)

        self.set_timer()

    # Creating input fields
    def set_timer(self):
       # Creating text input field for savings window
        savings_text = tk.Label(self, text = "Amount of days to lock.", font = fonts.header2_font, bg="#F5F5F0", fg="#333333")
        savings_text.grid(row = 8, column = 0, pady=10)
        self.savings_input = tk.Entry(self, font=fonts.body_font)
        self.savings_input.grid(row = 9, column = 0, pady=10)


        # Creating button and calling information storage on click.
        savings_button = tk.Button(self, text="Lock account", command=self.set_locked_period,
        font=fonts.button_font, bg="#F5F5F0", fg="#333333",bd=0, highlightbackground="#F5F5F0")
        savings_button.grid(row = 10, column = 0, pady=10)


    def set_locked_period(self):
        # Validation to lock account
        todays_date = datetime.now()
        days_locked = int(self.savings_input.get())

        if days_locked <= 0:
            messagebox.showinfo("Error", "Days inputted must be more than 0.")
        else:
            locked_until_date = str(todays_date + timedelta(days=days_locked))
            locked_until_date = locked_until_date[:10] 

            all_accounts = db_queries.get_bank_accounts()
            all_accounts[self.user_id][self.account_id]["locked_until_date"] = locked_until_date
            db_queries.write_to_accounts_json(all_accounts)
            db_queries.toggle_locked_account(self.user_id, self.account_id)

            messagebox.showinfo("Success", f"Account locked until {locked_until_date}")
            self.destroy()
