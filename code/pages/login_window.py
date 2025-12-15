import tkinter as tk
import tkinter.font as tkFont
import backend.password_checker as password_checker
import backend.db_queries as db_queries
import pages.landing_page as landing_page
import pages.sign_up_window as sign_up_window

# Login user will save the user_id in cache-file and destroy the window if successful
# If login fails, nothing will happen
def login_user():
    saved_info = dict()
    saved_info['personal_number'] = login_window.personal_number.get()
    saved_info['password'] = login_window.user_password.get()

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
            login_window.withdraw() # hides the login window

            # opens the landing page, passing the user_id of the logged in user and the login_window (as the parent)
            landing_page.load_window(logged_in_user, login_window)
            return logged_in_user
        except FileNotFoundError:
            print("Cache not found")
            return ""
        
def display_login():
    personal_number_label = tk.Label(login_window, text="Personal Number:", bg="#B6B6B6")
    personal_number_label.grid(column=0, row=1, padx=10, pady=10, sticky="e")

    login_window.personal_number = tk.Entry(login_window)
    login_window.personal_number.grid(column=1, row=1, padx=10, pady=10, sticky="w")

    # Password
    password_label = tk.Label(login_window, text="Password:", bg="#B6B6B6")
    password_label.grid(column=0, row=2, padx=10, pady=10, sticky="e")

    login_window.user_password = tk.Entry(login_window, show="*")
    login_window.user_password.grid(column=1, row=2, padx=10, pady=10, sticky="w")

    login_button = tk.Button(login_window, text="Login", command =login_user)
    login_button.grid(column=1, row=3, pady=20)

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
    login_window.geometry('600x400')
    login_window.configure(bg="#B6B6B6")

    ROWS = 5
    COLUMNS = 3

    for i in range(COLUMNS):
        login_window.columnconfigure(i, weight=1)
    for i in range(ROWS):
        login_window.rowconfigure(i, weight=1)

    header_font = tkFont.Font(family="Times", size=25, weight="bold")

    header = tk.Label(login_window, text="Bankino", bg="#B6B6B6", font=header_font)
    header.grid(column=1, row=0, sticky=tk.NSEW, pady=10)
    
    # Sign up button
    # pressing the button will call the function to open sign up page and hide the login window
    signup_button = tk.Button(login_window, text="Sign up", command = open_signup_window) 
    signup_button.grid(column=0, row=3, pady=20)

    display_login()
    login_window.protocol("WM_DELETE_WINDOW", close_program)
    return login_window # returns created tk.TK() window, which is used to start gui from main
