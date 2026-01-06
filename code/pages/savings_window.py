import tkinter as tk
import fonts.bankino_fonts as fonts
from tkinter import ttk, messagebox
from datetime import datetime, timedelta
import backend.db_queries as db_queries


def set_timer(account_id, user_id):

    # Creating text input field for savings window
    savings_text = tk.Label(savings_window, text = "Amount of days to lock.", font = fonts.header2_font, bg="#F5F5F0", fg="#333333")
    savings_text.grid(row = 8, column = 0, pady=10)
    savings_input = tk.Entry(savings_window, font=fonts.body_font)
    savings_input.grid(row = 9, column = 0, pady=10)


    # Creating button and calling information storage on click.
    savings_button = tk.Button(savings_window, text="Lock account", command=lambda: set_locked_period(savings_input.get(), account_id, user_id),
    font=fonts.button_font, bg="#F5F5F0", fg="#333333",bd=0, highlightbackground="#F5F5F0")
    savings_button.grid(row = 10, column = 0, pady=10)

def set_locked_period(savings_input, account_id, user_id):

    # Getting dates to write to database.
    todays_date = datetime.now()
    days_locked = int(savings_input)

    if days_locked <= 0:
        messagebox.showinfo("Error", f"Days inputted must be more than 0.")
    else: 
        locked_until_date = str(todays_date + timedelta(days=days_locked))
        locked_until_date = locked_until_date[:10] # Slicing at 10 to save only year, month, day.

        #Dumping the locked date to database
        all_accounts = db_queries.get_bank_accounts()
        all_accounts[user_id][account_id]["locked_until_date"] = locked_until_date
        db_queries.write_to_accounts_json(all_accounts)
        db_queries.toggle_locked_account(user_id, account_id)
        messagebox.showinfo("Success", f"Account locked until {locked_until_date}")
        
        savings_window.destroy()






def load_window(account_id, previous_window, user_id): 
    global savings_window
    global back_window 
    back_window = previous_window
        
    savings_window = tk.Toplevel(previous_window) # creates a new window on top of the previous one, uses Toplevel instead of Tk since.
    savings_window.title(f"Account: {account_id}")
    savings_window.geometry('600x600')
    savings_window.configure(bg="#F5F5F0")
    savings_window.resizable(width=False, height=False)
    
    # Configures the amount of columns and rows
    ROWS = 20
    COLUMNS = 20
    for i in range(COLUMNS):
        savings_window.columnconfigure(i, weight = 1)
    for i in range(ROWS):
        savings_window.rowconfigure(i, weight = 1)

    nav_bar = tk.Frame(savings_window, bg="#5D866C", width=600, height=124)
    nav_bar.place(x=0, y=0)

    header = tk.Label(savings_window, text="Bankino", font=fonts.header_font, bg="#5D866C", fg="#F5F5F0")
    header.place(x=20, y=16)

    set_timer(account_id, user_id)