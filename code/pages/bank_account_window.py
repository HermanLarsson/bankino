import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk, messagebox
import backend.db_queries as db_queries
import pages.transaction_history as transaction_history
import pages.savings_window as savings_window
import pages.show_card_window as show_card_window
import fonts.bankino_fonts as fonts
from tkinter.simpledialog import askstring

def delete_account(user_id, account_id):
    
    if messagebox.askquestion("Are you sure?", "Do you really want to remove the account " + account_id + "?", type="yesno") == "yes":
        all_accounts = db_queries.get_bank_accounts_by_user(user_id)

        if all_accounts[account_id]['balance'] > 0.0:
            messagebox.showinfo("Error", "Cannot remove an account with balance!")
            return
        elif all_accounts[account_id]['balance'] < 0.0:
            messagebox.showinfo("Error", "Cannot delete account in debt.")
            return
        elif all_accounts[account_id]['balance'] == 0.0:
            try: 
                db_queries.delete_bank_account(user_id, account_id)
                messagebox.showinfo("Success!", "Your account has been deleted.")
                return True
            except:
                messagebox.showerror("Error!", "An unknown error occured when trying to remove the account")
                return
    else:
        return
    
def clear_window():
    for widget in bank_account_window.winfo_children():
            widget.destroy()
    

def show_nav_bar():
        header = tk.Label(bank_account_window, text = "Bankino", font = fonts.header_font)
        header.grid(column = 0, row = 0, sticky = tk.NSEW)
        separator = ttk.Separator(bank_account_window, orient = "horizontal")
        separator.place(relx=0, rely=0.1, relwidth=1, relheight=0)


# Then take a Bank ID to access the specific bank account details. 
def show_account_data(user_id, account_id):

    clear_window()
    all_accounts = db_queries.get_bank_accounts_by_user(user_id)

    show_nav_bar()
    # data for the individual account the user wants to display
    account_data = all_accounts[account_id]

    if account_data['account_type'] == "SAV":
        
        if account_data['savings_goal'] == 0:
            print("Creating Butoné")
            create_goal_button = tk.Button(bank_account_window, text="Create Savings Goal", font=fonts.button_font, bg="#FFFFFF", fg="#333333", bd = 0, highlightbackground="#F5F5F0", command=lambda: True if not create_savings_goal(user_id, account_id, account_data['balance']) else show_account_data(user_id, account_id))
            create_goal_button.place(relx=0.13, rely=0.68)
        
        elif account_data['savings_goal'] > 0:
            current_amount = account_data['balance']
            savings_goal = account_data['savings_goal']
            goal_percent = 100*(current_amount / savings_goal)
            
            savings_goal_title = tk.Label(bank_account_window, text=f"Savings Goal: " + str(round(goal_percent, 2)) + "%", font= fonts.header2_font)
            savings_goal_title.place(relx=0.1, rely=0.73)

            savings_goal_bar_bg = tk.Frame(bank_account_window, bg="#bbc4bd", width = 800, height = 60)
            savings_goal_bar_bg.place(relx=0.1, rely=0.8)

            savings_goal_bar_fg = tk.Frame(bank_account_window, bg="#5D866C", width=(goal_percent*10), height= 60)
            savings_goal_bar_fg.place(relx=0.1, rely=0.8)

            delete_savings_goal_button = tk.Button(bank_account_window, text="Delete Savings Goal", bg="#FFFFFF", fg="red", bd = 0, highlightbackground="#F5F5F0", command=lambda: True if not delete_savings_goal(user_id, account_id) else show_account_data(user_id, account_id))
            delete_savings_goal_button.place(relx = 0.1, rely = 0.9)

            savings_goal_bar_text = tk.Label(bank_account_window, text=f"{current_amount}SEK / {savings_goal}SEK", font=fonts.value_font)
            savings_goal_bar_text.place(relx= 0.9, rely= 0.87, anchor="ne")


    # all of the labels holding acocunt data to be shown on the page
    title = tk.Label(bank_account_window, text = f"Account: {account_id}", font = fonts.header2_font)
    title.grid (column = 0, row = 1, sticky='w')

    account_balance = tk.Label(bank_account_window, text = (f"Balance: "), font = fonts.header2_font, anchor = "w")
    account_balance.grid(column = 0, row = 3, sticky = 'w')

    account_balance_value = tk.Label(bank_account_window, text = (f"{account_data['balance']} {account_data['currency']}"), font = fonts.value_font, anchor = "w")
    account_balance_value.grid(column = 0, row = 4, sticky = 'w')

    account_name = tk.Label(bank_account_window, text = (f"Account Name: {account_data['account_name']}"), font = fonts.body_font, anchor = "w")
    account_name.grid(column = 0, row = 6, sticky = 'w')

    account_type = tk.Label(bank_account_window, text = (f"Account Type: {account_data['account_type']}"), font = fonts.body_font, anchor = "w")
    account_type.grid(column = 0, row = 7, sticky = 'w')

    account_currency = tk.Label(bank_account_window, text = (f"Currency: {account_data['currency']}"), font = fonts.body_font, anchor = "w")
    account_currency.grid(column = 0, row = 8, sticky = 'w')

    view_transactions_button = tk.Button(bank_account_window, text="Transaction History", command=lambda: open_transaction_window(user_id, account_id))
    view_transactions_button.grid(column = 2, row = 10, sticky = 'w')

    delete_button = tk.Button(bank_account_window, text = "Delete account", fg="red", bg="#FFFFFF", font=fonts.button_font, command=lambda:  True if not delete_account(user_id, account_id) else  back_to_landing_page())
    delete_button.grid(column=17, row=3, sticky='w')

    if account_data['card_connected']:
        view_card_button = tk.Button(bank_account_window, text="View card", command=lambda: show_card_window.load_window(bank_account_window, user_id, account_data["card_number"]))
        view_card_button.grid(column = 0, row = 10, sticky = "w")
    else:
        order_card_button = tk.Button(bank_account_window, text="Order card", command=lambda: order_card())
        order_card_button.grid(column = 0, row = 10, sticky = "w")

    if account_data['account_type'] == "SAV":
        lock_account_button = tk.Button(bank_account_window, text="Lock Account", command=lambda: toggle_lock(user_id, account_id))
        lock_account_button.grid(column = 3, row = 10, sticky = 'w')

        back_to_landing_page_button = tk.Button(bank_account_window, text="Back to Landing Page", command=back_to_landing_page)
        back_to_landing_page_button.grid(column = 6, row = 10, sticky = 'w')
    else:
        back_to_landing_page_button = tk.Button(bank_account_window, text="Back to Landing Page", command=back_to_landing_page)
        back_to_landing_page_button.grid(column = 8, row = 10, sticky = 'w')


def order_card():
    pass
    #DON'T WANT TO FINISH THIS
    #CAN TAKE FARZAMS STUFF TO DO THIS ONE
    #PROB WON'T BE HERE EITHER


def open_transaction_window(user_id, account_id):
    bank_account_window.withdraw() #hides the accounts window
    transaction_history.load_window(user_id, account_id, bank_account_window) #opens transaction history window

def toggle_lock(user_id, account_id):
    users_accounts = db_queries.get_bank_accounts_by_user(user_id)
    if not users_accounts[account_id]["is_locked"]:
        savings_window.load_window(account_id, bank_account_window, user_id)
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

def create_savings_goal(user_id, account_id, balance):
    save_value = askstring('Goal', 'How much would you like to save?')
    try:    
        save_value = int(save_value)
    except:
        messagebox.showerror("Error", "You must enter a number!")
        return False
    if save_value < 0 or save_value > 1000000000:
        messagebox.showerror("Error", "You can not save that amount of money, what the helly!?")
        return False
    elif save_value < balance:
        messagebox.showerror("Error", "You already have that much money.")
        return False
    else:
        db_queries.add_savings_goal_to_account(user_id, account_id, save_value)
        return True

def delete_savings_goal(user_id, account_id):
   print("del savings goal called")
   try:
       print("Trying to delete goal...")
       db_queries.delete_savings_goal(user_id, account_id)
       #clear_window()
       return True
   except:
       return False

def back_to_landing_page():
    bank_account_window.withdraw()
    back_window.deiconify() #Brings back the landing page.

# display the banks details on the screen. 
def load_window(user_id, account_id, previous_window): 
    global bank_account_window
    global back_window 
    back_window = previous_window
        
    bank_account_window = tk.Toplevel(previous_window) # creates a new window on top of the previous one, uses Toplevel instead of Tk since.
    bank_account_window.title(f"Account: {account_id}")
    bank_account_window.geometry('1000x1000')

    # Configures the amount of columns and rows
    ROWS = 20
    COLUMNS = 20
    for i in range(COLUMNS):
        bank_account_window.columnconfigure(i, weight = 1)
    for i in range(ROWS):
        bank_account_window.rowconfigure(i, weight = 1)

    show_account_data(user_id, account_id)
    