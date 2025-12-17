import tkinter as tk
from tkinter import messagebox
import tkinter.font as tkFont
import backend.password_checker as password_checker
import backend.db_queries as db_queries


class AccountManagementWindow(tk.Toplevel):

    def __init__(self, parent, user_id):
        super().__init__(parent)

        self.title("Account Management")
        self.geometry("600x600")
        self.configure(bg="#B6B6B6")

        self.grid_layout()
        self.create_header()
        self.display_account_management(user_id)


    def grid_layout(self):
        # configure the grid
        ROWS = 15
        COLUMNS = 3
        for i in range(COLUMNS):
            self.columnconfigure(i, weight=1)
        for i in range(ROWS):
            self.rowconfigure(i, weight=1)


    def create_header(self):
        # Header
        header_font = tkFont.Font(family="Times", size=25, weight="bold")
        header = tk.Label(self, text="Bankino", bg="#B6B6B6", font=header_font)
        header.grid(column=1, row=0, sticky="w", pady=10)


    def display_account_management(self, user_id):
        # loads the user data from database
        user_data = db_queries.get_user_info(user_id)

        # first name 
        first_name_label = tk.Label(self, text="First Name:", bg="#B6B6B6")
        first_name_label.grid(column=0, row=1, padx=10, pady=10, sticky="e")
        self.first_name_entry = tk.Entry(self)
        self.first_name_entry.grid(column=1, row=1, padx=10, pady=10, sticky="w")
        
        # middle name 
        middle_name_label = tk.Label(self, text="Middle Name:", bg="#B6B6B6")
        middle_name_label.grid(column=0, row=2, padx=10, pady=10, sticky="e")
        self.middle_name_entry = tk.Entry(self)
        self.middle_name_entry.grid(column=1, row=2, padx=10, pady=10, sticky="w")
        
        # last name
        last_name_label = tk.Label(self, text="Last Name:", bg="#B6B6B6")
        last_name_label.grid(column=0, row=3, padx=10, pady=10, sticky="e")
        self.last_name_entry = tk.Entry(self)
        self.last_name_entry.grid(column=1, row=3, padx=10, pady=10, sticky="w")
        
        # phone number
        phone_label = tk.Label(self, text="Phone Number:", bg="#B6B6B6")
        phone_label.grid(column=0, row=4, padx=10, pady=10, sticky="e")
        self.phone_entry = tk.Entry(self)
        self.phone_entry.grid(column=1, row=4, padx=10, pady=10, sticky="w")
        
        # email
        email_label = tk.Label(self, text="Email:", bg="#B6B6B6")
        email_label.grid(column=0, row=5, padx=10, pady=10, sticky="e")
        self.email_entry = tk.Entry(self)
        self.email_entry.grid(column=1, row=5, padx=10, pady=10, sticky="w")
        
        # address
        address_label = tk.Label(self, text="Address:", bg="#B6B6B6")
        address_label.grid(column=0, row=6, padx=10, pady=10, sticky="e")
        self.address_entry = tk.Entry(self)
        self.address_entry.grid(column=1, row=6, padx=10, pady=10, sticky="w")
    

        # current password 
        current_password_label = tk.Label(self, text="Current Password:", bg="#B6B6B6")
        current_password_label.grid(column=0, row=7, padx=10, pady=10, sticky="e")
        self.current_password_entry = tk.Entry(self, show="*")
        self.current_password_entry.grid(column=1, row=7, padx=10, pady=10, sticky="w")
    
        # new password 
        new_password_label = tk.Label(self, text="New Password:", bg="#B6B6B6")
        new_password_label.grid(column=0, row=8, padx=10, pady=10, sticky="e")
        self.new_password_entry = tk.Entry(self, show="*")
        self.new_password_entry.grid(column=1, row=8, padx=10, pady=10, sticky="w")

        # confirm new password
        confirm_password_label = tk.Label(self, text="Confirm Password:", bg="#B6B6B6")
        confirm_password_label.grid(column=0, row=9, padx=10, pady=10, sticky="e")
        self.confirm_password_entry = tk.Entry(self, show="*")
        self.confirm_password_entry.grid(column=1, row=9, padx=10, pady=10, sticky="w")

        # inserts for the fields from the database
        self.first_name_entry.insert(0, user_data["first_name"])  
        self.middle_name_entry.insert(0, user_data["middle_name"])
        self.last_name_entry.insert(0, user_data["last_name"]) 

        # inserts phone if it is in database else empty string
        if "phone" in user_data:
            self.phone_entry.insert(0, user_data["phone"])
        else:
            self.phone_entry.insert(0, "")

        # inserts email if it is in database else empty string
        if "email" in user_data:
            self.email_entry.insert(0, user_data["email"])
        else:
            self.email_entry.insert(0, "")

        # inserts address if it is in database else empty string
        if "address" in user_data:
            self.address_entry.insert(0, user_data["address"])
        else:
            self.address_entry.insert(0, "")

        # save button 
        save_button = tk.Button(self, text="Save", command=lambda: self.update_account_info(user_id))
        save_button.grid(column=1, row=10, pady=20, sticky="w")


    #Gets all the information from
    def update_account_info(self, user_id):
        
        new_info = {}
        new_info['first_name'] = self.first_name_entry.get()
        new_info['middle_name'] = self.middle_name_entry.get()
        new_info['last_name'] = self.last_name_entry.get()
        new_info['phone'] = self.phone_entry.get()
        new_info['email'] = self.email_entry.get()
        new_info['address'] = self.address_entry.get()
        #new_info['curr_pass'] = password_checker.hash_password(curr_pass)
        new_info['password'] = password_checker.hash_password(self.new_password_entry.get())
        #new_info['confirm_pass'] = password_checker.hash_password(confirm_pass)

        curr_pass = password_checker.hash_password(self.current_password_entry.get())
        confirm_pass = password_checker.hash_password(self.confirm_password_entry.get())

        current_user_info = db_queries.get_user_info(user_id)

        errors = []
        error_message = ""
        
        if db_queries.verify_user(current_user_info['personal_number'], curr_pass) == user_id:
            if new_info['first_name'] == '':
                errors.append("You must have a first name!")
            if new_info['last_name'] == '':
                errors.append("You must have a last name!")
            if new_info['password'] != confirm_pass:
                errors.append("Passwords don't match!")
        else:
            errors.append("You have entered an incorrect password!")

        if len(errors) > 0:
            for error in errors:
                error_message += (error + '\n')
            messagebox.showerror("Error", error_message)
            return False
        else:
            if db_queries.update_user_info(user_id, new_info):
                messagebox.showinfo("Success!", "Your account has been updated!")
                return True
            else:
                messagebox.showerror("Error", "An error occured while saving the account information. Please panic.")
                return False


     


    









    


    


    