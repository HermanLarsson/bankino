import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk, messagebox
from datetime import datetime, timedelta

def set_timer():
    savings_text = tk.Label(savings_window, text = "Amount of days to lock.", font = header2_font)
    savings_text.grid(row = 0, column = 0)
    savings_input = tk.Entry(savings_window)
    savings_input.grid(row = 1, column = 0)

    savings_button = tk.Button(savings_window, text= "Lock account", command = lambda : get_info(savings_input.get()))
    savings_button.grid(row = 2, column = 0)


def get_info(savings_input):
    todays_date = datetime.now()
    days_locked = int(savings_input)
    locked_until_date = todays_date + timedelta(days=days_locked)
    print(locked_until_date)



def load_window(account_id, previous_window): 
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

    set_timer()