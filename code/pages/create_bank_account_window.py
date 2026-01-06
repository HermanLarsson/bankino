import tkinter as tk
from tkinter import *
import fonts.bankino_fonts as tkFont
import backend.create_bank_account as create_bank_account
import pages.landing_page as landing_page


class CreateBankAccount(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.title('Bankino')
        self.geometry('600x600')
        self.configure(bg="#F5F5F0") #Configures background

        self.grid_layout()
        self.create_header()
        self.display_create_bank_account()
    

    def grid_layout(self):
        ROWS = 20
        COLUMNS = 20
        for i in range(COLUMNS):
            self.columnconfigure(i, weight=1)
        for i in range(ROWS):
            self.rowconfigure(i, weight=1)

    
    def create_header(self):
           # Nav bar
        nav_bar = tk.Frame(self, bg="#5D866C", width=600, height=124)
        nav_bar.place(x=0, y=0)
    
    # Header
        header = tk.Label(self, text="Create Bank Account", bg="#5D866C", fg="#F5F5F0", font=tkFont.header_font)
        header.place(x=20, y=16)
    

    def display_create_bank_account(self):
        account_name_label = tk.Label(self, text="Account Name:", bg="#F5F5F0", fg="#333333", font=tkFont.body_font)
        account_name_label.grid(column=0, row=11, padx=10, pady=10, sticky="e")

        self.account_name = tk.Entry(self, font=tkFont.body_font)
        self.account_name.grid(column=1, row=11, padx=10, pady=10, sticky="w")


        account_types = [
            "SAV (Savings Account)", 
            "ISK (Investments Savings Account)", 
            "CHK (Check Account)", 
            "CAS (Casino Account)"]
        
        self.account_type = StringVar(self, "CAS (Casino Account)")

        #Radio button menu
        curr_row = 12
        for lang in account_types:
            curr_row += 1
            curr = Radiobutton(self, text=lang, variable=self.account_type, value=lang, bg="#F5F5F0", fg="#333333", font=tkFont.body_font)
            curr.grid(column=1, row=curr_row, padx=1, pady=1, sticky="w")

        # Initialize needs_card as False by default
        self.needs_card = BooleanVar(self, False)

        # Generate card checkbox
        generate_card_checkbox = tk.Checkbutton(self, text="Order Card", variable=self.needs_card, bg="#F5F5F0", fg="#333333", font=tkFont.body_font)
        generate_card_checkbox.grid(column=1, row=18, pady=10, sticky="w")

        #"Create new bank account" buttom
        create_button = tk.Button(self, text="Create New Bank Account", command=self.run_create_new_account,
                          font=tkFont.button_font, bg="#F5F5F0", fg="#333333", bd=0, highlightbackground="#F5F5F0")
        create_button.grid(column=1, row=19, pady=10, sticky="w")


    #Calls the function that creates and stores a new bank account in data/bank_accounts/accounts.json
    #Need the run_create_new_account() to be able to pass parameters to create_new_account()
    def run_create_new_account(self):
        chosen_type = self.account_type.get()
        chosen_name = self.account_name.get()
        card_needed = self.needs_card.get()
        try:
            create_bank_account.create_new_account(chosen_type[:3] , chosen_name , card_needed)
            self.destroy()
        except KeyError:
            print("KeyError in create_new_account")
            print(chosen_type[:3])
            print(chosen_name)
