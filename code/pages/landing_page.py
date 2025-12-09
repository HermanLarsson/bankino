import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk
import backend.db_queries as db_queries
import pages.create_bank_account_window as create_bank_account_window
import pages.bank_account as bank_account
import pages.deposit_funds_window as deposit_funds_window
import pages.transfer_funds_window as transfer_funds_window
from datetime import date
import pages.account_management_window as account_management_window

account_headers = []
account_amounts = []
account_buttons = []

#Loops through the lists to destroy the widges one by one
#After that it clears the lists so that new widgets can take their place.
#Lastly, we call list_accounts to print them anew.
def refresh_accounts(user_id): 

    for i in range(0, len(account_buttons)):
        account_headers[i].destroy()
        account_amounts[i].destroy()
        account_buttons[i].destroy()

    account_headers.clear()
    account_amounts.clear()
    account_buttons.clear()

    list_accounts(user_id)

#Creates labels for each accounts id, name and amount as well as button
def list_accounts(user_id):
    account_counter = 0
    current_row = 3
    bank_accounts = db_queries.load_bank_accounts(user_id)
    for account in bank_accounts.items():
        account_headers.append(tk.Label(landing_page, text = (account[0] + "  " + account[1]["account_name"]), font = header3_font, anchor = "w"))
        account_headers[account_counter].grid(column = 0, row = current_row, sticky = "w")
        
        account_amounts.append(tk.Label(landing_page, text = (str(account[1]["balance"]) + " SEK"), font = value_font))
        account_amounts[account_counter].grid(column = 4, row = current_row)

        account_buttons.append(tk.Button(landing_page, text="View Account Details", command=lambda clicked_id = account[0] : OnButtonClick(user_id ,clicked_id)))
        account_buttons[account_counter].grid(row = current_row + 1, column = 0, sticky = "NW")

        current_row += 2
        account_counter += 1

def OnButtonClick(user_id, clicked_id):
    landing_page.withdraw()
    bank_account.load_window(user_id, clicked_id, landing_page)

# Checking if locked savings account date has passed.
def check_date(user_id):
    todays_date = str(date.today())
    all_accounts = db_queries.load_all_bank_accounts()
    users_accounts = all_accounts[user_id]

    for account, data in users_accounts.items():
        if data["is_locked"]:
            locked_until_date = data["locked_until_date"]
            if convert_dates(todays_date) > convert_dates(locked_until_date):
                print("Checking date function")
                db_queries.toggle_locked_account(user_id, account)
            else:
                pass
                # Dominics stuff

def convert_dates(date_string):
    year = date_string[0:4]
    month = date_string [5:7]
    day = date_string [8:10]
    return date(int(year), int(month), int(day))

        


#Program starts here
#Main functions which runs the program
def load_window(user_id, login_window):
    check_date(user_id)
    global landing_page 
    # uses Toplevel instead of Tk since it is a 'child' window
    landing_page = tk.Toplevel(login_window) #Creates the window
    landing_page.title('Bankino')
    landing_page.geometry('1000x1000')
    #landing_page.configure(bg = "#B6B6B6") #Configures the background
    #Configures the amount of columns and rows
    ROWS = 20
    COLUMNS = 20
    for i in range(COLUMNS):
        landing_page.columnconfigure(i, weight = 1)
    for i in range(ROWS):
        landing_page.rowconfigure(i, weight = 1)

    #Three different header fonts for each weight.
    global header3_font
    global header_font
    global header2_font
    global value_font

    header3_font = tkFont.Font(family="Calibri", size = 20, weight = "bold")
    header_font = tkFont.Font(family = "Calibri", size = 30, weight = "bold")
    header2_font = tkFont.Font(family="Calibri", size = 25, weight = "bold")
    value_font = tkFont.Font(family = "Courier", size = 15, weight = "normal")

    #Creates the header as a Label over the entire cell
    header = tk.Label(landing_page, text = "Bankino", font = header_font)
    header.grid(column=0, row=0, sticky=tk.NSEW)
    title = tk.Label(landing_page, text = "Accounts", font = header2_font)
    title.grid (column = 0, row = 1)
    separator = ttk.Separator(landing_page, orient = "horizontal")
    separator.place(relx=0, rely=0.1, relwidth=1, relheight=0)

    #Creates create new bank account button
    create_bank_account_button = tk.Button(landing_page, text="Create New Bank Account", command=lambda: create_bank_account_window.load_window(landing_page, user_id))
    create_bank_account_button.grid(column=19, row=0, sticky="nswe")

    # Deposit funds button
    deposit_funds_button = tk.Button(landing_page, text="Deposit Funds", command=lambda: deposit_funds_window.load_window(landing_page, user_id))
    deposit_funds_button.grid(column = 18, row = 0, sticky = "nswe")

    # Transfer funds button
    transfer_funds_button = tk.Button(landing_page, text="Transfer Funds", command=lambda: transfer_funds_window.load_window(landing_page, user_id))
    transfer_funds_button.grid(column = 17, row = 0, sticky = "nsew")
        
    refresh_button = tk.Button(landing_page, text="Refresh", command=lambda: refresh_accounts(user_id))
    refresh_button.grid(column = 15, row = 0, sticky = "nsew")

    # Account management button
    account_management_button = tk.Button(landing_page, text="Account", command=lambda: account_management_window.load_window(landing_page, user_id))
    account_management_button.grid(column= 15, row=0, sticky="nswe")

    list_accounts(user_id)
