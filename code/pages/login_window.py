import tkinter as tk
import tkinter.font as tkFont
import backend.password_checker as password_checker
import backend.db_queries as db_queries
from pages.landing_page import landing_page_window
import pages.sign_up_window as sign_up_window
import fonts.bankino_fonts as fonts


# This class is the root window, should only create one instance
# Class LoginWindow extends tk.Tk
class LoginWindow(tk.Tk):

    # Constructor function, calls all the GUI methods upon instantiation
    def __init__(self):

        # first, constructs the tk.Tk object 
        super().__init__()

        # Root window setup
        self.title("Bankino")
        self.geometry("600x400")
        self.configure(bg="#F5F5F0")
        fonts.initialize_fonts()

        nav_bar = tk.Frame(self, bg = "#5D866C", width = 1000, height = 124)
        nav_bar.place(x = 0, y = 0)

        # Methods that are called upon instantiation
        self.grid_layout()
        self.create_header()
        self.display_login()

        self.protocol("WM_DELETE_WINDOW", self.close_program)


    # GUI setup
    def grid_layout(self):
        ROWS = 5
        COLUMNS = 3

        for i in range(COLUMNS):
            self.columnconfigure(i, weight=1)
        for i in range(ROWS):
            self.rowconfigure(i, weight=1)


    def create_header(self):
        header = tk.Label(self, text="Bankino", font = fonts.header_font, fg="#F5F5F0", bg="#5D866C")
        header.place(x = 20, y = 16)


    def display_login(self):
        personal_number_label = tk.Label(self, text="Personal Number:", bg="#F5F5F0", font= fonts.body_font)
        personal_number_label.grid(column=0, row=2, padx=10, pady=10, sticky="e")
        personal_number_label.config(fg="#333333")

        self.personal_number = tk.Entry(self)
        self.personal_number.grid(column=1, row=2, padx=10, pady=10, sticky="w")

        password_label = tk.Label(self, text="Password:", bg="#F5F5F0", font= fonts.body_font)
        password_label.grid(column=0, row=3, padx=10, pady=10, sticky="e")
        password_label.config(fg="#333333")

        self.user_password = tk.Entry(self, show="*")
        self.user_password.grid(column=1, row=3, padx=10, pady=10, sticky="w")

        login_button = tk.Button(self, text="Login", command =self.login_user, bg="#F5F5F0",font = fonts.button_font, bd = 0, highlightbackground = "#F5F5F0")
        login_button.grid(column=1, row=4, pady=10)
        login_button.config(fg="#333333")


        # Sign up button
        # pressing the button will call the function to open sign up page and hide the login window
        signup_button = tk.Button(self, text="Sign up", command = self.open_signup_window, bg="#F5F5F0",font = fonts.button_font, bd = 0, highlightbackground = "#F5F5F0",) 
        signup_button.grid(column=0, row=4, pady=10, sticky="e")
        signup_button.config(fg="#333333")



    def login_user(self):
        saved_info = dict()
        saved_info['personal_number'] = self.personal_number.get()
        saved_info['password'] = self.user_password.get()

        hashed_password = password_checker.hash_password(saved_info["password"])

        try: 
            personal_number = int(saved_info["personal_number"])
        except TypeError:
            print("Personal number must be digits only")
            return ""
        
        # user_id is returned as a string, which is what gets passed through each window of the program to load user data
        logged_in_user = db_queries.verify_user(personal_number, hashed_password)
        if logged_in_user == "":
            print("Invalid credentials.")
            return logged_in_user
        else:
            try:
                db_queries.write_to_cache(logged_in_user)
                print("Login successful.")
                self.withdraw() # hides the login window

                # opens the landing page, passing the user_id of the logged in user and the login_window (as the parent)
                landing_page_window(logged_in_user, self)
                return logged_in_user
            except FileNotFoundError:
                print("Cache not found")
                return ""
            
    def open_signup_window(self):
        self.withdraw() # hides the login window
        sign_up_window.load_window(self) # opens the sign up window

    # closes the window when the user exists the program
    def close_program(self):
        self.destroy()