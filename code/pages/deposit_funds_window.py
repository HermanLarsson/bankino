import backend.db_queries as db_queries
import tkinter as tk
import tkinter.font as tkFont

account_buttons = []

def create_account_choices(avail_accounts):
    account_counter = 0
    current_row = 6
    for account in avail_accounts.items():
        print("CURRENT ACCOUNT ::::::::", account)
        account_buttons.append(tk.Radiobutton(deposit_funds_window, text = account[0] + " - " + account[1]['account_name']))
        account_buttons[account_counter].grid(column = 0, row = current_row)
        current_row += 1
        account_counter += 1


def load_window(parent, user_id):
    avail_accounts = db_queries.get_all_account_data(user_id)

    global deposit_funds_window
    # uses Toplevel instead of Tk since it is a 'child' window
    deposit_funds_window = tk.Toplevel(parent) #Creates the window
    deposit_funds_window.title('Bankino')
    deposit_funds_window.geometry('600x400')
       
    #Configures the amount of columns and rows
    ROWS = 20
    COLUMNS = 20
    for i in range(COLUMNS):
        deposit_funds_window.columnconfigure(i, weight=1)
    for i in range(ROWS):
        deposit_funds_window.rowconfigure(i, weight=1)

    global header2_font
    header2_font = tkFont.Font(family="Calibri", size = 25, weight = "bold")

    window_label = tk.Label(deposit_funds_window, text="Deposit Funds")
    window_label.grid(column=0, row=1, padx=10, pady=10, sticky="e")

    amount_label = tk.Label(deposit_funds_window, text="Amount:")
    amount_label.grid(column=0, row=4, padx=10, pady=10, sticky="e")

    amount_entry = tk.Entry(deposit_funds_window)
    amount_entry.grid(column=1, row=4, padx=10, pady=10, sticky="w")
    
    create_account_choices(avail_accounts)

    confirm_button = tk.Button(deposit_funds_window, text = "Deposit", command=lambda: print("Bababooey"))
    confirm_button.grid(column=5, row=10, sticky="S")

