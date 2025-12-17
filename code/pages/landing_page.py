import tkinter as tk
from tkinter import ttk
import backend.db_queries as db_queries

import pages.bank_account_window as bank_account_window
import pages.deposit_funds_window as deposit_funds_window
import pages.transfer_funds_window as transfer_funds_window
from datetime import date
from pages.account_management_window import AccountManagementWindow
from pages.create_bank_account_window import CreateBankAccount
import fonts.bankino_fonts as fonts



#Program starts here
#Main functions which runs the program
class landing_page_window(tk.Toplevel):

    def __init__(self, user_id, parent):
        super().__init__(parent)

        # uses Toplevel instead of Tk since it is a 'child' window
        self.title('Bankino')
        self.geometry('1000x1000')
        self.configure(bg="#F5F5F0")
        self.resizable(width=False, height=False)

        self.account_headers = []
        self.account_amounts = []
        self.account_buttons = []

        self.verify_locked_account_date(user_id)
        self.grid_layout()
        self.create_nav_bar()
        self.create_headers()
        self.create_nav_bar_buttons(user_id)
        self.list_accounts(user_id)

        # calls the function to terminate the program when the user closes the landing page
        self.protocol("WM_DELETE_WINDOW", lambda: self.close_landing_page(parent))


    def grid_layout(self):
        #Configures the amount of columns and rows
        ROWS = 20
        COLUMNS = 10
        for i in range(COLUMNS):
            self.columnconfigure(i, weight = 1)
        for i in range(ROWS):
            self.rowconfigure(i, weight = 1)

    def create_nav_bar(self):
        nav_bar = tk.Frame(self, bg = "#5D866C", width = 1000, height = 124)
        nav_bar.place(x = 0, y = 0)

    def create_headers(self):
        #Creates the header as a Label over the entire cell
        header = tk.Label(self, text = "Bankino", font = fonts.header_font, fg="#F5F5F0", bg="#5D866C")
        header.place(x = 20, y = 16)
        title = tk.Label(self, text = "Accounts", font = fonts.header2_font, fg="#333333", bg="#F5F5F0")
        title.place (x = 20, y = 136)
        separator = ttk.Separator(self, orient = "horizontal")
        separator.place(relx=0, y=124, relwidth=1, relheight=0,)

    def create_nav_bar_buttons(self, user_id):
        #Account Management Button
        account_management_button = tk.Button(self, text="Account", fg="#333333", bg="#FFFFFF", bd=0, highlightbackground = "#5D866C", font = fonts.nav_font, command=lambda: AccountManagementWindow(self, user_id))
        account_management_button.place(x = 347, y = 30)

        #Refresh Button
        refresh_button = tk.Button(self, text="Refresh", fg="#333333", bg="#FFFFFF", bd=0, highlightbackground = "#5D866C", font = fonts.nav_font, command=lambda: self.refresh_accounts(user_id))
        refresh_button.place(x = 461, y = 30)

        # Transfer funds button
        transfer_funds_button = tk.Button(self, text="Transfer", fg="#333333", bg="#FFFFFF", bd=0, highlightbackground = "#5D866C", font = fonts.nav_font, command=lambda: transfer_funds_window.load_window(self, user_id))
        transfer_funds_button.place(x = 571, y = 30)

        # Deposit funds button
        deposit_funds_button = tk.Button(self, text="Deposit", fg="#333333", bg="#FFFFFF", bd=0, highlightbackground = "#5D866C", font = fonts.nav_font, command=lambda: deposit_funds_window.load_window(self, user_id))
        deposit_funds_button.place(x = 690, y = 30)

        #Creates create new bank account button
        create_bank_account_button = tk.Button(self, text="Create Account", fg="#333333", bg="#FFFFFF", bd=0, highlightbackground = "#5D866C", font = fonts.nav_font, command=lambda: CreateBankAccount(self))
        create_bank_account_button.place(x = 800, y = 30)

    #Creates labels for each accounts id, name and amount as well as button
    def list_accounts(self, user_id):
        account_counter = 0
        current_row = 5
        bank_accounts = db_queries.get_user_bank_accounts(user_id)

        for account in bank_accounts.items():
            self.account_headers.append(tk.Label(self, text = (account[0] + "  " + account[1]["account_name"]), font = fonts.body_font, fg="#333333", bg="#F5F5F0", anchor = "w"))
            self.account_headers[account_counter].grid(column = 1, row = current_row, sticky = "w")

            self.account_amounts.append(tk.Label(self,  text = (str(account[1]["balance"]) + " SEK"), font = fonts.value_font, fg="#333333", bg="#F5F5F0"))
            self.account_amounts[account_counter].grid(column = 4, row = current_row, sticky ="w")

            self.account_buttons.append(tk.Button(self, text="View Account Details", font = fonts.button_font, fg="#333333", bg="#F5F5F0", bd = 0, highlightbackground = "#F5F5F0", command=lambda clicked_id = account[0] : self.on_button_click(user_id, clicked_id)))
            self.account_buttons[account_counter].grid(column = 1, row = current_row + 1, sticky = "nw")

            current_row += 2
            account_counter += 1

    #Loops through the lists to destroy the widges one by one
    #After that it clears the lists so that new widgets can take their place.
    #Lastly, we call list_accounts to print them anew.
    def refresh_accounts(self, user_id): 

        for i in range(0, len(self.account_buttons)):
            self.account_headers[i].destroy()
            self.account_amounts[i].destroy()
            self.account_buttons[i].destroy()

        self.account_headers.clear()
        self.account_amounts.clear()
        self.account_buttons.clear()

        self.list_accounts(user_id)

    def on_button_click(self, user_id, clicked_id):
        self.withdraw()
        bank_account_window.load_window(user_id, clicked_id, self)

    # Checking if locked savings account date has passed.
    def verify_locked_account_date(self, user_id):
        todays_date = str(date.today())
        users_accounts = db_queries.get_user_bank_accounts(user_id)

        try:
            for account, data in users_accounts.items():
                if data["is_locked"]:
                    locked_until_date = data["locked_until_date"]
                    if todays_date > locked_until_date:
                        print("Checking date function")
                        db_queries.toggle_locked_account(user_id, account)
                        return True
        except KeyError:
            print(f"Error: {KeyError}")

        return False

    # called when the user closes the landing page to destroy mainloop in login window to terminate program
    def close_landing_page(self, login_window):
        login_window.destroy()