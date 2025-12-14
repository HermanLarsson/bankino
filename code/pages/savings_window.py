import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk, messagebox
from datetime import datetime, timedelta
import backend.db_queries as db_queries


def set_timer(account_id, user_id):

    # Creating text input field for savings window
    savings_text = tk.Label(savings_window, text = "Amount of days to lock.", font = header2_font)
    savings_text.grid(row = 0, column = 0)
    savings_input = tk.Entry(savings_window)
    savings_input.grid(row = 1, column = 0)


    # Creating button and calling information storage on click.
    savings_button = tk.Button(savings_window, text= "Lock account", command = lambda : set_locked_period(savings_input.get(), account_id, user_id))
    savings_button.grid(row = 2, column = 0)

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
    savings_window.geometry('250x250')
    # Configures the amount of columns and rows
    ROWS = 20
    COLUMNS = 20
    for i in range(COLUMNS):
        savings_window.columnconfigure(i, weight = 1)
    for i in range(ROWS):
        savings_window.rowconfigure(i, weight = 1)

    # Different fonts/formatting for labels
    global header2_font
    global header_font
    global value_font
    global header3_font

    header_font = tkFont.Font(family = "Calibri", size = 30, weight = "bold")
    header2_font = tkFont.Font(family = "Calibri", size = 20, weight = "bold")
    value_font = tkFont.Font(family = "Courier", size = 30, weight = "normal")
    header3_font = tkFont.Font(family = "Calibri", size = 20, weight = "normal")


    header = tk.Label(savings_window, text = "Bankino", font = header_font)
    header.grid(column = 0, row = 0, sticky = tk.NSEW)
    separator = ttk.Separator(savings_window, orient = "horizontal")
    separator.place(relx=0, rely=0.1, relwidth=1, relheight=0)

    set_timer(account_id, user_id)