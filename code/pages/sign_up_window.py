import tkinter as tk
import tkinter.font as tkFont
import backend.db_queries as db_queries
import tkinter.messagebox as messagebox
import re
import backend.password_checker as password_checker
from datetime import date
import fonts.bankino_fonts as fonts


class SignUpWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        self.title('Bankino')
        self.geometry('600x600')
        self.configure(bg="#F5F5F0")


        self.create_nav_bar()
        self.grid_layout()
        self.create_headers()
        self.display_signup()

        self.protocol("WM_DELETE_WINDOW", self.close_sign_up)


    def create_nav_bar(self):
        nav_bar = tk.Frame(self, bg = "#5D866C", width = 1000, height = 124)
        nav_bar.place(x = 0, y = 0)


    def grid_layout(self):
        ROWS, COLUMNS = 8, 3
        for i in range(COLUMNS):
            self.columnconfigure(i, weight=1)
        for i in range(ROWS):
            self.rowconfigure(i, weight=1)


    def create_headers(self):
        header = tk.Label(self, text = "Bankino", font = fonts.header_font, fg="#F5F5F0", bg="#5D866C")
        header.place(x = 20, y = 16)


    def get_date(self):
        todays_date = str(date.today())
        return todays_date


    def sign_up_user(self):
        # get inputs
        first_name_input = self.first_name_entry.get()
        last_name_input = self.last_name_entry.get()
        middle_name_input = self.middle_name_entry.get()
        personal_number_input = self.personal_number_entry.get()
        join_date = self.get_date()
        password_input = self.user_password_entry.get()

         # Checking if inputs have the requirments.
        # Name should only contain letters.
        name_regex = r"^[A-Za-z]+$"
        # Middle name should only contain letters or be empty.
        middle_name_regex = r"^[A-Za-z]*$"
        # Personal number should contain 10 or 12 digits.
        personal_number_regex = r"^\d{10}(\d{2})?$"
        if not re.fullmatch(name_regex, first_name_input):
            messagebox.showerror("Error", "First name must contain letters.")
            return
        if not re.fullmatch(name_regex, last_name_input):
            messagebox.showerror("Error", "Last name must contain letters.")
            return
        if not re.fullmatch(middle_name_regex, middle_name_input):
            messagebox.showerror("Error", "Middle name must contain only letters or be empty.")
            return
        if not re.fullmatch(personal_number_regex, personal_number_input):
            messagebox.showerror("Error", "Personal number must be 10 or 12 digits.") 
            return
        # Password must contain at least 8 characters.
        if not password_checker.password_vailidity_check(password_input):
            return

        # Call the sign up function
        db_queries.sign_up(first_name_input, last_name_input, middle_name_input,
                        personal_number_input, join_date, password_checker.hash_password(password_input))
        # Show massage user account created successfully!
        messagebox.showinfo("Success", "User account created successfully!")
        self.back_to_login()


    def back_to_login(self):
        self.destroy()   # destroys/closes the sign up window
        self.parent.deiconify()

    # takes user back to login window when closing the sign up window
    def close_sign_up(self):
        self.back_to_login()


    def display_signup(self):  
        # First Name
        self.first_name_entry = tk.Entry(self)
        self.first_name_entry.grid(column=1, row=3, padx=10, pady=10, sticky="w")
        first_name_label = tk.Label(self, text="First Name:", font=fonts.body_font, bg="#F5F5F0")
        first_name_label.grid(column=0, row=3, padx=10, pady=10, sticky="e")
        first_name_label.config(fg="#333333")

        # Last Name
        self.last_name_entry = tk.Entry(self)
        self.last_name_entry.grid(column=1, row=4, padx=10, pady=10, sticky="w")
        last_name_label = tk.Label(self, text="Last Name:", font=fonts.body_font, bg="#F5F5F0")
        last_name_label.grid(column=0, row=4, padx=10, pady=10, sticky="e")
        last_name_label.config(fg="#333333")

        # Middle Name
        self.middle_name_entry = tk.Entry(self)
        self.middle_name_entry.grid(column=1, row=5, padx=10, pady=10, sticky="w")
        middle_name_label = tk.Label(self, text="Middle Name:", font=fonts.body_font, bg="#F5F5F0")
        middle_name_label.grid(column=0, row=5, padx=10, pady=10, sticky="e")
        middle_name_label.config(fg="#333333")

        # Personal Number
        self.personal_number_entry = tk.Entry(self) 
        self.personal_number_entry.grid(column=1, row=6, padx=10, pady=10, sticky="w")
        personal_number_label = tk.Label(self, text="Personal Number:", font=fonts.body_font, bg="#F5F5F0")
        personal_number_label.grid(column=0, row=6, padx=10, pady=10, sticky="e")
        personal_number_label.config(fg="#333333")

        # Password
        self.user_password_entry = tk.Entry(self, show="*")
        self.user_password_entry.grid(column=1, row=7, padx=10, pady=10, sticky="w")
        password_label = tk.Label(self, text="Password:", font=fonts.body_font, bg="#F5F5F0")
        password_label.grid(column=0, row=7, padx=10, pady=10, sticky="e")
        password_label.config(fg="#333333")

        # Sign Up button
        signup_button = tk.Button(self, text="Sign Up", font=fonts.body_font, command=self.sign_up_user, fg="#333333")
        signup_button.grid(column=1, row=8, pady=20)

        # back to login button
        back_button = tk.Button(self, text= "Back to Login", font=fonts.body_font, command = self.back_to_login)
        back_button.grid(column=0, row=8, pady=20)

