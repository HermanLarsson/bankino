import tkinter as tk
from tkinter import messagebox
import fonts.bankino_fonts as fonts
import backend.password_checker as password_checker
import backend.db_queries as db_queries
from tkinter import ttk


class AccountManagementWindow(tk.Toplevel):

    def __init__(self, parent, user_id):
        super().__init__(parent)

        self.title("Account Management")
        self.geometry("600x600")
        self.configure(bg="#F5F5F0")
        self.resizable(width=False, height=False)

        self.grid_layout()
        self.create_header()
        self.display_account_management(user_id)


    def grid_layout(self):
        # configure the grid
        ROWS = 20
        COLUMNS = 20
        for i in range(COLUMNS):
            self.columnconfigure(i, weight=1)
        for i in range(ROWS):
            self.rowconfigure(i, weight=1)


    def create_header(self):

        nav_bar = tk.Frame(self, bg="#5D866C", width=600, height=124)
        nav_bar.place(x=0, y=0)

        header = tk.Label(self, text="Bankino", font=fonts.header_font, bg="#5D866C", fg="#F5F5F0")
        header.place(x=20, y=16)


    def display_account_management(self, user_id):

        canvas = tk.Canvas(self, bg="#F5F5F0", highlightthickness=0)
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg="#F5F5F0")
        scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.place(x=0, y=124, width=580, height=400) 
        scrollbar.place(x=580, y=124, width=20, height=400) 

        # loads the user data from database
        user_data = db_queries.get_user_info(user_id)

        # first name input field
        first_name_label = tk.Label(scrollable_frame, text="First Name:", bg="#F5F5F0", fg="#333333", font=fonts.body_font)
        first_name_label.grid(column=0, row=6, padx=10, pady=10, sticky="e")
        self.first_name_entry = tk.Entry(scrollable_frame, font=fonts.body_font)
        self.first_name_entry.grid(column=1, row=6, padx=10, pady=10, sticky="w")
        
        # middle name input field
        middle_name_label = tk.Label(scrollable_frame, text="Middle Name:", bg="#F5F5F0", fg="#333333", font=fonts.body_font)
        middle_name_label.grid(column=0, row=7, padx=10, pady=10, sticky="e")
        self.middle_name_entry = tk.Entry(scrollable_frame, font=fonts.body_font)
        self.middle_name_entry.grid(column=1, row=7, padx=10, pady=10, sticky="w")
        
        # last name input field
        last_name_label = tk.Label(scrollable_frame, text="Last Name:", bg="#F5F5F0", fg="#333333", font=fonts.body_font)
        last_name_label.grid(column=0, row=8, padx=10, pady=10, sticky="e")
        self.last_name_entry = tk.Entry(scrollable_frame, font=fonts.body_font)
        self.last_name_entry.grid(column=1, row=8, padx=10, pady=10, sticky="w")
        
        # phone number input field
        phone_label = tk.Label(scrollable_frame, text="Phone Number:", bg="#F5F5F0", fg="#333333", font=fonts.body_font)
        phone_label.grid(column=0, row=9, padx=10, pady=10, sticky="e")
        self.phone_entry = tk.Entry(scrollable_frame, font=fonts.body_font)
        self.phone_entry.grid(column=1, row=9, padx=10, pady=10, sticky="w")
        
        # email input field
        email_label = tk.Label(scrollable_frame, text="Email:", bg="#F5F5F0", fg="#333333", font=fonts.body_font)
        email_label.grid(column=0, row=10, padx=10, pady=10, sticky="e")
        self.email_entry = tk.Entry(scrollable_frame, font=fonts.body_font)
        self.email_entry.grid(column=1, row=10, padx=10, pady=10, sticky="w")
        
        # address input field
        address_label = tk.Label(scrollable_frame, text="Address:", bg="#F5F5F0", fg="#333333", font=fonts.body_font)
        address_label.grid(column=0, row=11, padx=10, pady=10, sticky="e")
        self.address_entry = tk.Entry(scrollable_frame, font=fonts.body_font)
        self.address_entry.grid(column=1, row=11, padx=10, pady=10, sticky="w")
    
        # current password input field
        current_password_label = tk.Label(scrollable_frame, text="Current Password:", bg="#F5F5F0", fg="#333333", font=fonts.body_font)
        current_password_label.grid(column=0, row=12, padx=10, pady=10, sticky="e")
        self.current_password_entry = tk.Entry(scrollable_frame, show="*", font=fonts.body_font)
        self.current_password_entry.grid(column=1, row=12, padx=10, pady=10, sticky="w")
    
        # new password input field
        new_password_label = tk.Label(scrollable_frame, text="New Password:", bg="#F5F5F0", fg="#333333", font=fonts.body_font)
        new_password_label.grid(column=0, row=13, padx=10, pady=10, sticky="e")
        self.new_password_entry = tk.Entry(scrollable_frame, show="*", font=fonts.body_font)
        self.new_password_entry.grid(column=1, row=13, padx=10, pady=10, sticky="w")

        # confirm new password input field
        confirm_password_label = tk.Label(scrollable_frame, text="Confirm Password:", bg="#F5F5F0", fg="#333333", font=fonts.body_font)
        confirm_password_label.grid(column=0, row=14, padx=10, pady=10, sticky="e")
        self.confirm_password_entry = tk.Entry(scrollable_frame, show="*", font=fonts.body_font)
        self.confirm_password_entry.grid(column=1, row=14, padx=10, pady=10, sticky="w")

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
        save_button = tk.Button(self, text="Save", command=lambda: self.update_account_info(user_id), font=fonts.button_font, bg="#F5F5F0",
        fg="#333333",bd=0, highlightbackground="#F5F5F0")
        save_button.place(x=250, y=550)


    #Gets all the information from
    def update_account_info(self, user_id):
        current_user_info = db_queries.get_user_info(user_id)

        new_info = {
            'first_name': self.first_name_entry.get(),
            'middle_name': self.middle_name_entry.get(),
            'last_name': self.last_name_entry.get(),
            'phone': self.phone_entry.get(),
            'email': self.email_entry.get(),
            'address': self.address_entry.get(),
            'password': password_checker.hash_password(self.new_password_entry.get())
        }

        current_pass = password_checker.hash_password(self.current_password_entry.get())
        new_password = password_checker.hash_password(self.new_password_entry.get())
        confirm_pass = password_checker.hash_password(self.confirm_password_entry.get())

        errors = []
        error_message = ""
        
        if db_queries.verify_user(current_user_info['personal_number'], current_pass) == user_id:
            if new_info['first_name'] == '':
                errors.append("You must have a first name!")
            if new_info['last_name'] == '':
                errors.append("You must have a last name!")
            if new_password != confirm_pass:
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
                self.close_program()
                return True
            else:
                messagebox.showerror("Error", "An error occured while saving the account information. Please panic.")
                return False


    # closes the window when the user exists the program
    def close_program(self):
        self.destroy()


    









    


    


    