import tkinter as tk
import tkinter.font as tkFont
import backend.password_checker as password_checker
import backend.db_queries as db_queries
import pages.landing_page as landing_page
import pages.sign_up_window as sign_up_window
import fonts.bankino_fonts as fonts

# Login user will save the user_id in cache-file and destroy the window if successful
# If login fails, nothing will happen
def login_user():
    saved_info = dict()
    saved_info['personal_number'] = personal_number.get()
    saved_info['password'] = user_password.get()
    print(saved_info)

    hashed_password = password_checker.hash_password(saved_info["password"])

    login_check = db_queries.verify_user(int(saved_info["personal_number"]), hashed_password)
    if login_check == "":
        print("Invalid credentials.")
        try:
            with open ("./data/cache/logged_in_user.cache", "w") as file:
                file.write(login_check)
        except FileNotFoundError:
            print("Cache not found")
    else:
        print("Login successful.")
        try:
            with open ("./data/cache/logged_in_user.cache", "w") as file:
                file.write(login_check)
        except FileNotFoundError:
            print("Cache not found")
        login_window.withdraw() # hides the login window
        landing_page.load_window(login_check, login_window) # opens the landing page
        
def display_login():
    personal_number_label = tk.Label(login_window, text="Personal Number:", bg="#F5F5F0")
    personal_number_label.grid(column=0, row=1, padx=10, pady=10, sticky="e")
    personal_number_label.config(fg="#333333",)

    global personal_number
    global user_password

    personal_number = tk.Entry(login_window)
    personal_number.grid(column=1, row=1, padx=10, pady=10, sticky="w")
    personal_number.config(fg="#333333")

    # Password
    password_label = tk.Label(login_window, text="Password:", bg="#F5F5F0")
    password_label.grid(column=0, row=2, padx=10, pady=10, sticky="e")
    password_label.config(fg="#333333")

    user_password = tk.Entry(login_window, show="*")
    user_password.grid(column=1, row=2, padx=10, pady=10, sticky="w")
    user_password.config(fg="#333333")

    login_button = tk.Button(login_window, text="Login", command =login_user, bg="#F5F5F0",font = fonts.button_font, bd = 0, highlightbackground = "#F5F5F0",)
    login_button.grid(column=1, row=3, pady=10)
    login_button.config(fg="#333333")

def open_signup_window():
    login_window.withdraw() # hides the login window
    sign_up_window.load_window(login_window) # opens the sign up window

# closes the window when the user exists the program
def close_program():
    login_window.destroy()

def load_window():
   
    global login_window
    login_window = tk.Tk()  # Creates the window
    login_window.title('Bankino')
    login_window.geometry('600x600')
    login_window.configure(bg="#F5F5F0")
    fonts.initialize_fonts()

    nav_bar = tk.Frame(login_window, bg = "#5D866C", width = 1000, height = 124)
    nav_bar.place(x = 0, y = 0)

    ROWS = 5
    COLUMNS = 3

    for i in range(COLUMNS):
        login_window.columnconfigure(i, weight=1)
    for i in range(ROWS):
        login_window.rowconfigure(i, weight=1)

    header = tk.Label(login_window, text="Bankino", font = fonts.header_font, fg="#F5F5F0", bg="#5D866C")
    header.place(x = 20, y = 16)
    
    # Sign up button
    # pressing the button will call the function to open sign up page and hide the login window
    signup_button = tk.Button(login_window, text="Sign up", command = open_signup_window, bg="#F5F5F0",font = fonts.button_font, bd = 0, highlightbackground = "#F5F5F0",) 
    signup_button.grid(column=0, row=3, padx=5, sticky="e")
    signup_button.config(fg="#333333")

    display_login()
    login_window.protocol("WM_DELETE_WINDOW", close_program)
    return login_window # returns created tk.TK() window, which is used to start gui from main
