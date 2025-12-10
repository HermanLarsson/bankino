import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk
import backend.db_queries as db_queries
import pages.create_bank_account_window as create_bank_account_window
import pages.bank_account as bank_account
import pages.deposit_funds_window as deposit_funds_window
import pages.transfer_funds_window as transfer_funds_window
import pages.account_management_window as account_management_window
import fonts.bankino_fonts as fonts

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
    current_row = 4
    bank_accounts = db_queries.load_bank_accounts(user_id)
    for account in bank_accounts.items():
        account_headers.append(tk.Label(landing_page, text = (account[0] + "  " + account[1]["account_name"]), font = body_font, fg="#333333", anchor = "w", bg="#F5F5F0"))
        account_headers[account_counter].grid(column = 0, row = current_row, sticky = "w")
        
        account_amounts.append(tk.Label(landing_page,  text = (str(account[1]["balance"]) + " SEK"), font = value_font, fg="#333333", bg="#F5F5F0"))
        account_amounts[account_counter].grid(column = 4, row = current_row, sticky ="w")

        account_buttons.append(tk.Button(landing_page, text="View Account Details", bg="#F5F5F0",font = button_font, fg="#333333", bd = 0, highlightbackground = "#F5F5F0", command=lambda clicked_id = account[0] : OnButtonClick(user_id ,clicked_id)))
        account_buttons[account_counter].grid(row = current_row + 1, column = 0, sticky = "NW")

        current_row += 2
        account_counter += 1

def OnButtonClick(user_id, clicked_id):
    landing_page.withdraw()
    bank_account.load_window(user_id, clicked_id, landing_page)

#Program starts here
#Main functions which runs the program
def load_window(user_id, parent):

    global landing_page
    
    # uses Toplevel instead of Tk since it is a 'child' window
    landing_page = tk.Toplevel(parent)#Creates the window
    landing_page.title('Bankino')
    landing_page.geometry('1000x1000')
    landing_page.configure(bg="#F5F5F0")
    landing_page.resizable(width=False, height=False)
    #landing_page.configure(bg = "#B6B6B6") #Configures the background
    #Configures the amount of columns and rows
    ROWS = 20
    COLUMNS = 10
    for i in range(COLUMNS):
        landing_page.columnconfigure(i, weight = 1)
    for i in range(ROWS):
        landing_page.rowconfigure(i, weight = 1)

    nav_bar = tk.Frame(landing_page, bg = "#5D866C", width = 1000, height = 124)
    nav_bar.place(x = 0, y = 0)

    #Creates the header as a Label over the entire cell
    header = tk.Label(landing_page, text = "Bankino", font = fonts.header_font, fg="#F5F5F0", bg="#5D866C")
    header.place(x = 20, y = 16)
    title = tk.Label(landing_page, text = "Accounts", font = fonts.header2_font, fg="#333333", bg="#F5F5F0")
    title.place (x = 20, y = 136)
    separator = ttk.Separator(landing_page, orient = "horizontal")
    separator.place(relx=0, y=124, relwidth=1, relheight=0,)

    #Account Management Button
    account_management_button = tk.Button(landing_page, text="Account", fg="#F5F5F0", bg="#5D866C", font = fonts.nav_font, bd = 0, highlightbackground = "#5D866C", command=lambda: account_management_window.load_window(landing_page, user_id))
    account_management_button.place(x = 347, y = 30)

    #Refresh Button
    refresh_button = tk.Button(landing_page, text="Refresh", bg="#5D866C", fg="#F5F5F0", font = fonts.nav_font, bd = 0, highlightbackground = "#5D866C", command=lambda: refresh_accounts(user_id))
    refresh_button.place(x = 461, y = 30)

    # Transfer funds button
    transfer_funds_button = tk.Button(landing_page, text="Transfer", fg="#F5F5F0", bg="#5D866C", font = fonts.nav_font, bd = 0, highlightbackground = "#5D866C", command=lambda: transfer_funds_window.load_window(landing_page, user_id))
    transfer_funds_button.place(x = 571, y = 30)

    # Deposit funds button
    deposit_funds_button = tk.Button(landing_page, text="Deposit", fg="#F5F5F0", bg="#5D866C", font = fonts.nav_font, bd = 0, highlightbackground = "#5D866C", command=lambda: deposit_funds_window.load_window(landing_page, user_id))
    deposit_funds_button.place(x = 690, y = 30)

    #Creates create new bank account button
    create_bank_account_button = tk.Button(landing_page, text="Create Account", fg="#F5F5F0", bg="#5D866C", font = fonts.nav_font, bd = 0, highlightbackground = "#5D866C", command=lambda: create_bank_account_window.load_window(landing_page, user_id))
    create_bank_account_button.place(x = 800, y = 30)

    

    
        
    

    

    list_accounts(user_id)
