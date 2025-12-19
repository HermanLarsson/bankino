import tkinter as tk
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
        self.geometry("250x250")

        # GUI setup
        ROWS = 20
        COLUMNS = 20
        for i in range(COLUMNS):
            self.columnconfigure(i, weight=1)
        for i in range(ROWS):
            self.rowconfigure(i, weight=1)

        # Create Header
        header = tk.Label(self, text="Bankino", font=fonts.header_font)
        header.grid(column=0, row=0, sticky=tk.NSEW)

        separator = ttk.Separator(self, orient="horizontal")
        separator.place(relx=0, rely=0.1, relwidth=1, relheight=0)

        self.set_timer()

    # Creating input fields
    def set_timer(self):
        savings_text = tk.Label(self, text="Amount of days to lock.", font=fonts.header2_font)
        savings_text.grid(row=0, column=0)

        self.savings_input = tk.Entry(self)
        self.savings_input.grid(row=1, column=0)

        # Creating button
        savings_button = tk.Button(self, text="Lock account", font=fonts.button_font, command=self.set_locked_period)
        savings_button.grid(row=2, column=0)


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
