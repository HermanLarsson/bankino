import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk, messagebox
import backend.db_queries as db_queries
import pages.transaction_history as transaction_history
import pages.savings_window as savings_window

# Then take a Bank ID to access the specific bank account details. 
def show_account_data(user_id, account_id):
    all_accounts = db_queries.get_all_account_data(user_id)

    # data for the individual account the user wants to display
    account_data = all_accounts[account_id]

    # all of the labels holding acocunt data to be shown on the page
    title = tk.Label(bank_account, text = f"Account: {account_id}", font = header2_font)
    title.grid (column = 0, row = 1, sticky='w')

    account_balance = tk.Label(bank_account, text = (f"Balance: "), font = header2_font, anchor = "w")
    account_balance.grid(column = 0, row = 3, sticky = 'w')

    account_balance_value = tk.Label(bank_account, text = (f"{account_data['balance']} {account_data['currency']}"), font = value_font, anchor = "w")
    account_balance_value.grid(column = 0, row = 4, sticky = 'w')

    account_name = tk.Label(bank_account, text = (f"Account Name: {account_data['account_name']}"), font = header3_font, anchor = "w")
    account_name.grid(column = 0, row = 6, sticky = 'w')

    account_type = tk.Label(bank_account, text = (f"Account Type: {account_data['account_type']}"), font = header3_font, anchor = "w")
    account_type.grid(column = 0, row = 7, sticky = 'w')

    account_currency = tk.Label(bank_account, text = (f"Currency: {account_data['currency']}"), font = header3_font, anchor = "w")
    account_currency.grid(column = 0, row = 8, sticky = 'w')

    view_transactions_button = tk.Button(bank_account, text="View Transaction History", command=lambda: open_transaction_window(user_id, account_id))
    view_transactions_button.grid(column = 0, row = 9, sticky = 'w')

    if account_data['account_type'] == "SAV":
        lock_account_button = tk.Button(bank_account, text="Lock Account", command=lambda: toggle_lock(user_id, account_id))
        lock_account_button.grid(column = 0, row = 10, sticky = 'w')

        back_to_landing_page_button = tk.Button(bank_account, text="Back to Landing Page", command=back_to_landing_page)
        back_to_landing_page_button.grid(column = 0, row = 11, sticky = 'w')
    else:
        back_to_landing_page_button = tk.Button(bank_account, text="Back to Landing Page", command=back_to_landing_page)
        back_to_landing_page_button.grid(column = 0, row = 10, sticky = 'w')

def open_transaction_window(user_id, account_id):
    bank_account.withdraw() #hides the accounts window
    transaction_history.load_window(user_id, account_id, bank_account) #opens transaction history window

def toggle_lock(user_id, account_id):
    users_accounts = db_queries.get_all_account_data(user_id)
    if not users_accounts[account_id]["is_locked"]:
        savings_window.load_window(account_id, bank_account, user_id)
    else:
        # implement fine
        answer = messagebox.askquestion('Are you sure?', f'''Account {account_id} is already Locked.
                                        
                                        Are you sure you want to unlock Acount {account_id}?
                                        
                                        Unlocking early will incur a 100 SEK fine''')
        if answer == 'yes':
            db_queries.fine_user(user_id, account_id)
            messagebox.showinfo("Message", f'''Account {account_id} is unlocked
                                
                                100 SEK fine processed.''')
    db_queries.toggle_locked_account(user_id, account_id)
    return

    
def back_to_landing_page():
    bank_account.withdraw()
    back_window.deiconify() #Brings back the landing page.

# display the banks details on the screen. 
def load_window(user_id, account_id, previous_window): 
    global bank_account
    global back_window 
    back_window = previous_window
        
    bank_account = tk.Toplevel(previous_window) # creates a new window on top of the previous one, uses Toplevel instead of Tk since.
    bank_account.title(f"Account: {account_id}")
    bank_account.geometry('1000x1000')

    # Configures the amount of columns and rows
    ROWS = 20
    COLUMNS = 20
    for i in range(COLUMNS):
        bank_account.columnconfigure(i, weight = 1)
    for i in range(ROWS):
        bank_account.rowconfigure(i, weight = 1)

    # Different fonts/formatting for labels
    global header2_font
    global header_font
    global value_font
    global header3_font

    header_font = tkFont.Font(family = "Calibri", size = 30, weight = "bold")
    header2_font = tkFont.Font(family = "Calibri", size = 20, weight = "bold")
    value_font = tkFont.Font(family = "Courier", size = 30, weight = "normal")
    header3_font = tkFont.Font(family = "Calibri", size = 20, weight = "normal")


    header = tk.Label(bank_account, text = "Bankino", font = header_font)
    header.grid(column = 0, row = 0, sticky = tk.NSEW)
    separator = ttk.Separator(bank_account, orient = "horizontal")
    separator.place(relx=0, rely=0.1, relwidth=1, relheight=0)

    show_account_data(user_id, account_id)
    