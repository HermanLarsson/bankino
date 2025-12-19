import tkinter as tk
from tkinter import ttk, messagebox
import fonts.bankino_fonts as fonts
import backend.db_queries as db_queries
from tkinter.simpledialog import askstring
import pages.transaction_history_window as transaction_history_window
import pages.savings_window as savings_window
from pages.show_card_window import ShowCardWindow
import backend.generate_card as generate_card


class BankAccountWindow(tk.Toplevel):
    def __init__(self, user_id, account_id, parent):
        super().__init__(parent)

        # Makes parent accesible within the class
        self.parent = parent
        self.title(f"Account: {account_id}")
        self.geometry("1000x1000")
        self.grid_layout()

        self.show_account_data(user_id, account_id)
    
#-----------------------------------------------------------------
    # Configures the amount of columns and rows
    def grid_layout(self):
        ROWS = 20
        COLUMNS = 20
        for i in range(COLUMNS):
            self.columnconfigure(i, weight = 1)
        for i in range(ROWS):
            self.rowconfigure(i, weight = 1)

    def show_account_data(self, user_id, account_id):
    
        self.clear_window()
        all_accounts = db_queries.get_bank_accounts_by_user(user_id)
    
        self.show_nav_bar()
        # Data for the specific account the user entered
        account_data = all_accounts[account_id]
    
        if account_data['account_type'] == "SAV":
            
            if account_data['savings_goal'] == 0:
                print("Creating Butoné")
                create_goal_button = tk.Button(self, text="Create Savings Goal", font=fonts.button_font, bg="#FFFFFF", fg="#333333", bd = 0, highlightbackground="#F5F5F0", command=lambda: True if not self.create_savings_goal(user_id, account_id, account_data['balance']) else self.show_account_data(user_id, account_id))
                create_goal_button.place(relx=0.13, rely=0.68)
            
            elif account_data['savings_goal'] > 0:
                current_amount = account_data['balance']
                savings_goal = account_data['savings_goal']
                goal_percent = round(100*(current_amount / savings_goal), 2)
                
                savings_goal_title = tk.Label(self, text=f"Savings Goal: " + str(goal_percent) + "%", font= fonts.header2_font)
                savings_goal_title.place(relx=0.1, rely=0.73)
    
                savings_goal_bar_bg = tk.Frame(self, bg="#bbc4bd", height = 60)
                savings_goal_bar_bg.place(relx=0.1, rely=0.8, relwidth=0.8)
    
                savings_goal_bar_fg = tk.Frame(self, bg="#5D866C", height= 60)
                savings_goal_bar_fg.place(relx=0.1, rely=0.8, relwidth=(0.8*(goal_percent)/100))
    
                delete_savings_goal_button = tk.Button(self, text="Delete Savings Goal", bg="#FFFFFF", fg="red", bd = 0, highlightbackground="#F5F5F0", command=lambda: True if not self.delete_savings_goal(user_id, account_id) else self.show_account_data(user_id, account_id))
                delete_savings_goal_button.place(relx = 0.1, rely = 0.9)
    
                savings_goal_bar_text = tk.Label(self, text=f"{current_amount}SEK / {savings_goal}SEK", font=fonts.value_font)
                savings_goal_bar_text.place(relx= 0.9, rely= 0.87, anchor="ne")
    
    
        # Labels holding account data to be shown on the page
        title_label = tk.Label(self, text = f"Account: {account_id}", font = fonts.header2_font)
        title_label.grid (column = 0, row = 1, sticky='w')
    
        account_balance_label = tk.Label(self, text = (f"Balance: "), font = fonts.header2_font, anchor = "w")
        account_balance_label.grid(column = 0, row = 3, sticky = 'w')
    
        account_balance_value_label = tk.Label(self, text = (f"{account_data['balance']} {account_data['currency']}"), font = fonts.value_font, anchor = "w")
        account_balance_value_label.grid(column = 0, row = 4, sticky = 'w')
    
        account_name_label = tk.Label(self, text = (f"Account Name: {account_data['account_name']}"), font = fonts.body_font, anchor = "w")
        account_name_label.grid(column = 0, row = 6, sticky = 'w')
    
        account_type_label = tk.Label(self, text = (f"Account Type: {account_data['account_type']}"), font = fonts.body_font, anchor = "w")
        account_type_label.grid(column = 0, row = 7, sticky = 'w')
    
        account_currency_label = tk.Label(self, text = (f"Currency: {account_data['currency']}"), font = fonts.body_font, anchor = "w")
        account_currency_label.grid(column = 0, row = 8, sticky = 'w')
    
        view_transactions_button = tk.Button(self, text="Transaction History", command=lambda: self.open_transaction_window(user_id, account_id))
        view_transactions_button.grid(column = 2, row = 10, sticky = 'w')
    
        delete_button = tk.Button(self, text = "Delete account", fg="red", bg="#FFFFFF", font=fonts.button_font, command=lambda:  True if not self.delete_account(user_id, account_id) else  self.back_to_landing_page(self.parent))
        delete_button.grid(column=17, row=3, sticky='w')
    
        if account_data['card_connected']:
            view_card_button = tk.Button(self, text="View card", command=lambda: ShowCardWindow(self, user_id, account_data["card_number"]))
            view_card_button.grid(column = 0, row = 10, sticky = "w")
        else:
            order_card_button = tk.Button(self, text="Order card", command=lambda: generate_card.create_card(user_id, account_id))
            order_card_button.grid(column = 0, row = 10, sticky = "w")
    
        if account_data['account_type'] == "SAV":
            if account_data['is_locked'] == False:
                lock_account_button = tk.Button(self, text="Lock Account", command=lambda: self.toggle_lock(user_id, account_id))
                lock_account_button.grid(column = 3, row = 10, sticky = 'w')
            else:
                lock_account_button = tk.Button(self, text="Unlock Account", command=lambda: self.toggle_lock(user_id, account_id))
                lock_account_button.grid(column = 3, row = 10, sticky = 'w')
    
            back_to_landing_page_button = tk.Button(self, text="Back to Landing Page", command=lambda:self.back_to_landing_page(self.parent))
            back_to_landing_page_button.grid(column = 6, row = 10, sticky = 'w')
        else:
            back_to_landing_page_button = tk.Button(self, text="Back to Landing Page", command=lambda:self.back_to_landing_page(self.parent))
            back_to_landing_page_button.grid(column = 8, row = 10, sticky = 'w')
    
    def delete_account(self, user_id, account_id):
    
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
    
    def clear_window(self):
        for widget in self.winfo_children():
                widget.destroy()
        
    
    def show_nav_bar(self):
        header = tk.Label(self, text = "Bankino", font = fonts.header_font)
        header.grid(column = 0, row = 0, sticky = tk.NSEW)
        separator = ttk.Separator(self, orient = "horizontal")
        separator.place(relx=0, rely=0.1, relwidth=1, relheight=0)


    def open_transaction_window(self,user_id, account_id):
        self.withdraw() #hides the accounts window
        transaction_history_window.TransactionHistory(self, user_id, account_id) #opens transaction history window


    def toggle_lock(self, user_id, account_id):
        users_accounts = db_queries.get_bank_accounts_by_user(user_id)
        if not users_accounts[account_id]["is_locked"]:
            savings_window.SavingsWindow(self, account_id, user_id)
            return "Locked"
        else:
            answer = messagebox.askquestion('Are you sure?', f'''Account {account_id} is already Locked.

                                            Are you sure you want to unlock Acount {account_id}?

                                            Unlocking early will incur a 100 SEK fine''')
            if answer == 'yes':
                db_queries.fine_user(user_id, account_id)
                messagebox.showinfo("Message", f'''Account {account_id} is unlocked

                                    100 SEK fine processed.''')
                db_queries.toggle_locked_account(user_id, account_id)
                return "Unlocked"
            return "Still Locked"


    def create_savings_goal(self, user_id, account_id, balance):
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

    def delete_savings_goal(self, user_id, account_id):
       print("del savings goal called")
       try:
           print("Trying to delete goal...")
           db_queries.delete_savings_goal(user_id, account_id)
           return True
       except:
           return False

    def back_to_landing_page(self, parent):
        self.withdraw()
        parent.deiconify() #Brings back the landing page.