import tkinter as tk
import tkinter.font as tkFont
import backend.db_queries as db_queries
import tkinter.messagebox as messagebox
import re
import backend.password_checker as password_checker
from datetime import date
import fonts.bankino_fonts as fonts


def get_date():
    todays_date = str(date.today())
    return todays_date


def sign_up_user():
    # get inputs
    first_name_input = first_name_entry.get()
    last_name_input = last_name_entry.get()
    middle_name_input = middle_name_entry.get()
    personal_number_input = personal_number_entry.get()
    join_date = get_date()
    password_input = user_password_entry.get()


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

    
def display_signup():
    global first_name_entry, last_name_entry, middle_name_entry
    global personal_number_entry, user_password_entry

    first_name_entry = tk.Entry(sign_up_window)
    last_name_entry = tk.Entry(sign_up_window)
    middle_name_entry = tk.Entry(sign_up_window)
    personal_number_entry = tk.Entry(sign_up_window)
    user_password_entry = tk.Entry(sign_up_window, show="*")
    
    # First Name
    first_name_entry = tk.Entry(sign_up_window)
    first_name_entry.grid(column=1, row=3, padx=10, pady=10, sticky="w")
    first_name_label = tk.Label(sign_up_window, text="First Name:", font=fonts.body_font, bg="#F5F5F0")
    first_name_label.grid(column=0, row=3, padx=10, pady=10, sticky="e")
    first_name_label.config(fg="#333333")

    # Last Name
    last_name_entry = tk.Entry(sign_up_window)
    last_name_entry.grid(column=1, row=4, padx=10, pady=10, sticky="w")
    last_name_label = tk.Label(sign_up_window, text="Last Name:", font=fonts.body_font, bg="#F5F5F0")
    last_name_label.grid(column=0, row=4, padx=10, pady=10, sticky="e")
    last_name_label.config(fg="#333333")

    # Middle Name
    middle_name_entry = tk.Entry(sign_up_window)
    middle_name_entry.grid(column=1, row=5, padx=10, pady=10, sticky="w")
    middle_name_label = tk.Label(sign_up_window, text="Middle Name:", font=fonts.body_font, bg="#F5F5F0")
    middle_name_label.grid(column=0, row=5, padx=10, pady=10, sticky="e")
    middle_name_label.config(fg="#333333")

    # Personal Number
    personal_number_entry = tk.Entry(sign_up_window) 
    personal_number_entry.grid(column=1, row=6, padx=10, pady=10, sticky="w")
    personal_number_label = tk.Label(sign_up_window, text="Personal Number:", font=fonts.body_font, bg="#F5F5F0")
    personal_number_label.grid(column=0, row=6, padx=10, pady=10, sticky="e")
    personal_number_label.config(fg="#333333")

    # Password
    user_password_entry = tk.Entry(sign_up_window, show="*")
    user_password_entry.grid(column=1, row=7, padx=10, pady=10, sticky="w")
    password_label = tk.Label(sign_up_window, text="Password:", font=fonts.body_font, bg="#F5F5F0")
    password_label.grid(column=0, row=7, padx=10, pady=10, sticky="e")
    password_label.config(fg="#333333")

    # Sign Up button
    signup_button = tk.Button(sign_up_window, text="Sign Up", command=sign_up_user, bg="#F5F5F0",font = fonts.button_font, bd = 0, highlightbackground = "#F5F5F0")
    signup_button.grid(column=1, row=8, pady=20)
    signup_button.config(fg="#333333")

    # back to login button
    back_button = tk.Button(sign_up_window, text= "Back to Login", command = back_to_login, bg="#F5F5F0",font = fonts.button_font, bd = 0, highlightbackground = "#F5F5F0")
    back_button.grid(column=0, row=8, pady=20)
    back_button.config(fg="#333333")


def back_to_login():
    sign_up_window.destroy()   # destroys/closes the sign up window
    login_window.deiconify()

# takes user back to login window when closing the sign up window
def close_sign_up():
    back_to_login()

def load_window(previous_window):

    global sign_up_window, login_window

    login_window = previous_window # stores the login window in the background so it can be reopennd
    sign_up_window = tk.Toplevel(login_window) # Creates the sign up window on top of the login window

    sign_up_window.title('Bankino')
    sign_up_window.geometry('600x600')
    sign_up_window.configure(bg="#F5F5F0")

    nav_bar = tk.Frame(sign_up_window, bg = "#5D866C", width = 1000, height = 124)
    nav_bar.place(x = 0, y = 0)
    
    ROWS, COLUMNS = 8, 3
    for i in range(COLUMNS):
        sign_up_window.columnconfigure(i, weight=1)
    for i in range(ROWS):
        sign_up_window.rowconfigure(i, weight=1)
    

    header = tk.Label(sign_up_window, text = "Bankino", font = fonts.header_font, fg="#F5F5F0", bg="#5D866C")
    header.place(x = 20, y = 16)
     
    display_signup()

    # calls the function to take the user back to login window when closing sign up window
    sign_up_window.protocol("WM_DELETE_WINDOW", close_sign_up)
