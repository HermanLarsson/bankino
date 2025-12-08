import tkinter as tk
from tkinter import messagebox
import tkinter.font as tkFont 
import re
import backend.db_queries as db_queries 
import backend.logic_for_transfer_funds as transfer_funds

# Global variables
current_user_id = None 
transfer_funds_window = None

def display_transfer_funds():

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
        radiobutton = tk.Radiobutton(
            transfer_funds_window,
            text=f"{acc_id} ({acc_data['account_name']})",
            variable=from_account,
            value=acc_id,
            bg="#B6B6B6"
        )
        radiobutton.grid(column=1, row=curr_row, padx=1, pady=1, sticky="w")

    # To account label
    to_label = tk.Label(transfer_funds_window, text="Transfer to (account id):", bg="#B6B6B6")
    to_label.grid(column=0, row=curr_row + 2, padx=10, pady=10, sticky="e")

    to_account = tk.Entry(transfer_funds_window)
    to_account.grid(column=1, row=curr_row + 2, padx=10, pady=10, sticky="w")

    # Amount label
    amount_label = tk.Label(transfer_funds_window, text="Amount:", bg="#B6B6B6")
    amount_label.grid(column=0, row=curr_row + 3, padx=10, pady=10, sticky="e")

    amount = tk.Entry(transfer_funds_window)
    amount.grid(column=1, row=curr_row + 3, padx=10, pady=10, sticky="w")

    # confirm button
    confirm_button = tk.Button(transfer_funds_window, text="Confirm", command=lambda: process_transfer(from_account, to_account, amount))
    confirm_button.grid(column=1, row=curr_row + 5, pady=10, sticky="w")


def process_transfer(from_account, to_account, amount):
    print("Processing")
    # Saves the user input in varibles
    from_acc_input = from_account.get()
    to_acc_input = to_account.get()
    amount_input = amount.get()

    # Checks if user selected option on the radiobutton
    if from_acc_input == "":
        messagebox.showinfo("Error", "Select an account to transfer from")  
        return 
    
    # Checks if user inputted an account to transfer to
    if to_acc_input == "":
         messagebox.showinfo("Error", "Select an account to transfer to")
         return
    
    # Checks if user inputted an amount to transfer 
    if amount_input == "":
         messagebox.showinfo("Error", "Select an amount to transfer")
         return
    
    # Validate that to account exists in the database
    if not db_queries.check_account_exists(to_acc_input):
        messagebox.showinfo("Error", f"Account '{to_acc_input}' does not exist")
        return
    
    if to_acc_input == from_acc_input:
        messagebox.showinfo("Error", f"Can't transfer to the same account")
        return

    valid_input = r'\d+([.,]\d{2})?'
    if re.fullmatch(valid_input,amount_input):
        try: 
            amount_input = re.sub(r',', r'.', amount_input) # converts inputted coma to a dot
            amount_value = float(amount_input)

            # Checks if inputted amount is zero
            if amount_value == 0: 
                messagebox.showinfo("Error", "Input cannot be 0.00 SEK")
                return
            
            users_accounts = db_queries.get_all_account_data(current_user_id)
            current_balance = users_accounts[from_acc_input]['balance']
            
            has_sufficient_funds = transfer_funds.check_sufficient_funds(current_balance, amount_value)

            if not has_sufficient_funds:
                messagebox.showinfo("Error", f"Account {from_acc_input} does not has suffiecient funds for this transfer")  
                return
            
            # Calls the backend logic to transfer funds         
            transfer_funds.transfer_money(current_user_id, from_acc_input, to_acc_input, amount_value)
            print(f"{amount_value} successfully transferred from {from_acc_input} to {to_acc_input}")

            # Messege box for user when transfer succeded 
            messagebox.showinfo("Success", f"{amount_value:.2f} SEK successfully transfered from {from_acc_input} to {to_acc_input}")

            # Closes the pop-up window
            transfer_funds_window.destroy()

         # Throws error if inputted amount is not a float 
        except ValueError:
            print("Invalid amount entered")
            messagebox.showinfo("Error", "Invalid amount entered")
    else:
        print("amount has to be greater than 0")
        messagebox.showinfo("Error", "Input must be postive and have 0 or 2 decimal places")


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