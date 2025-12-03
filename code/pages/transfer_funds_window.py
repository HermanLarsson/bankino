import tkinter as tk 
import tkinter.font as tkFont 
import backend.db_queries as db_queries 

# Global variables holding user selections
from_account = None  
current_user_id = None 
to_account = None
amount = None

def display_transfer_funds():
    global from_account
    global to_account
    global amount

    # choose from accounts label
    from_label = tk.Label(transfer_funds_window, text="Choose account to transfer from:", bg="#B6B6B6")
    from_label.grid(column=0, row=1, padx=10, pady=10, sticky="e")
    
    # Get the user bank accounts
    accounts = db_queries.get_all_account_data(current_user_id)

    # Store which account the transfer is from
    from_account = tk.StringVar(transfer_funds_window)

    curr_row = 1
    for acc_id, acc_data in accounts.items():
        curr_row += 1
        curr = tk.Radiobutton(
            transfer_funds_window,
            text=f"{acc_id} ({acc_data['account_name']})",
            variable=from_account,
            value=acc_id,
            bg="#B6B6B6"
        )
        curr.grid(column=1, row=curr_row, padx=1, pady=1, sticky="w")

    # To account label
    to_label = tk.Label(transfer_funds_window, text="Transfer to (account id):", bg="#B6B6B6")
    to_label.grid(column=0, row=curr_row + 2, padx=10, pady=10, sticky="e")

    global to_account
    to_account = tk.Entry(transfer_funds_window)
    to_account.grid(column=1, row=curr_row + 2, padx=10, pady=10, sticky="w")

    # Amount label
    amount_label = tk.Label(transfer_funds_window, text="Amount:", bg="#B6B6B6")
    amount_label.grid(column=0, row=curr_row + 3, padx=10, pady=10, sticky="e")

    global amount
    amount = tk.Entry(transfer_funds_window)
    amount.grid(column=1, row=curr_row + 3, padx=10, pady=10, sticky="w")

    # confirm button
    confirm_button = tk.Button(transfer_funds_window, text="Confirm", command=transfer_funds) # 
    confirm_button.grid(column=1, row=curr_row + 5, pady=10, sticky="w")


def transfer_funds():
    # This function will run the logic
    print("DO LOGIC HERE")
    print("FROM:", from_account.get())
    print("TO:", to_account.get())
    print("AMOUNT:", amount.get())



def load_window(parent, user_id):
    global current_user_id
    current_user_id = user_id

    global transfer_funds_window
    transfer_funds_window = tk.Toplevel(parent) # Creates window 
    transfer_funds_window.title("Bankino - Transfer Funds")
    transfer_funds_window.geometry("600x400")
    transfer_funds_window.configure(bg="#B6B6B6") # Configures background

    # Configure grid layout
    ROWS = 20
    COLUMNS = 20
    for i in range(COLUMNS):
        transfer_funds_window.columnconfigure(i, weight=1)
    for i in range(ROWS):
        transfer_funds_window.rowconfigure(i, weight=1)

    # Header
    header_font = tkFont.Font(family="Times", size=25, weight="bold")
    header = tk.Label(transfer_funds_window, text="Bankino", bg="#B6B6B6", font=header_font)
    header.grid(column=1, row=0, sticky="w", pady=10)

    # Displays the GUI
    display_transfer_funds()
