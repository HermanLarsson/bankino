import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk
import json

logged_in_id = ""
bank_accounts = {}
account_headers = []
account_names = []
account_amounts = []




#Loads the users bank accounts. 
def load_bank_accounts(user_id):
    try:
        f = open("./data/bank_accounts/accounts.json")
        data = json.load(f)
        f.close()
    except FileNotFoundError:
        print("Databse file not found")
        
    if user_id in data.keys():
        for account in data[user_id].items():
            bank_accounts[account[0]] = account[1]
    else:
        print("nothing found")

#Creates labels for each accounts id, name and amount
def list_accounts():
    account_counter = 0
    current_row = 3
    for account in bank_accounts.items():
        account_headers.append(tk.Label(landing_page, text = (account[0] + "  " + account[1]["account_name"]), font = header3_font, anchor = "w"))
        account_headers[account_counter].grid(column = 0, row = current_row, sticky = "w")
        
        account_amounts.append(tk.Label(landing_page, text = (str(account[1]["balance"]) + " SEK"), font = value_font))
        account_amounts[account_counter].grid(column = 4, row = current_row)
        
        current_row += 2
        account_counter += 1


#Program starts here
#Main functions which runs the program


def main(user_id):

    global landing_page 
    landing_page = tk.Tk() #Creates the window
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

    load_bank_accounts(user_id)
    list_accounts()
    landing_page.mainloop() 

