import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk
import pages.bank_account as bank_account
import backend.db_queries as db_queries

logged_in_id = ""
bank_accounts = {}
account_headers = []
account_names = []
account_amounts = []
account_buttons = []

#Creates labels for each accounts id, name and amount
def list_accounts(user_id):
    account_counter = 0
    current_row = 3
    bank_accounts = db_queries.load_bank_accounts(user_id)
    for account in bank_accounts.items():
        account_headers.append(tk.Label(landing_page, text = (account[0] + "  " + account[1]["account_name"]), font = header3_font, anchor = "w"))
        account_headers[account_counter].grid(column = 0, row = current_row, sticky = "w")
        
        account_amounts.append(tk.Label(landing_page, text = (str(account[1]["balance"]) + " SEK"), font = value_font))
        account_amounts[account_counter].grid(column = 4, row = current_row)

        account_buttons.append(tk.Button(landing_page, text=account_counter, command=lambda clicked_id = account[0] : OnButtonClick(user_id ,clicked_id)))
        account_buttons[account_counter].grid(row = current_row + 1, column = 0, sticky = "NW")

        current_row += 2
        account_counter += 1

def OnButtonClick(user_id, clicked_id):
    landing_page.withdraw()
    bank_account.load_window(user_id, clicked_id, landing_page)

#Program starts here
#Main functions which runs the program


def load_window(user_id, login_window):

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

    #load_bank_accounts(user_id)
    list_accounts(user_id)
    