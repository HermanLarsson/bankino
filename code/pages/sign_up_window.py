import tkinter as tk
import tkinter.font as tkFont
import backend.sign_up as sign_up

def sign_up_user():
    # get inputs
    first_name_input = first_name_entry.get()
    join_date_input = join_date_entry.get()
    password_input = user_password_entry.get()   
    last_name_input = last_name_entry.get()
    personal_number_input = personal_number_entry.get()
    middle_name_input = middle_name_entry.get()


    # Call the sign up function
    sign_up.sign_up(first_name_input, last_name_input, middle_name_input,
                    personal_number_input, join_date_input, password_input)
    
def display_signup():
    global first_name_entry, last_name_entry, middle_name_entry
    global personal_number_entry, join_date_entry, user_password_entry

    first_name_entry = tk.Entry(sign_up_window)
    last_name_entry = tk.Entry(sign_up_window)
    middle_name_entry = tk.Entry(sign_up_window)
    personal_number_entry = tk.Entry(sign_up_window)
    join_date_entry = tk.Entry(sign_up_window)
    user_password_entry = tk.Entry(sign_up_window, show="*")
    
    # First Name
    first_name_entry = tk.Entry(sign_up_window)
    first_name_entry.grid(column=1, row=1, padx=10, pady=10, sticky="w")
    first_name_label = tk.Label(sign_up_window, text="First Name:", bg="#B6B6B6")
    first_name_label.grid(column=0, row=1, padx=10, pady=10, sticky="e")

    # Last Name
    last_name_entry = tk.Entry(sign_up_window)
    last_name_entry.grid(column=1, row=2, padx=10, pady=10, sticky="w")
    last_name_label = tk.Label(sign_up_window, text="Last Name:", bg="#B6B6B6")
    last_name_label.grid(column=0, row=2, padx=10, pady=10, sticky="e")

    # Middle Name
    middle_name_entry = tk.Entry(sign_up_window)
    middle_name_entry.grid(column=1, row=3, padx=10, pady=10, sticky="w")
    middle_name_label = tk.Label(sign_up_window, text="Middle Name:", bg="#B6B6B6")
    middle_name_label.grid(column=0, row=3, padx=10, pady=10, sticky="e")

    # Personal Number
    personal_number_entry = tk.Entry(sign_up_window)
    personal_number_entry.grid(column=1, row=4, padx=10, pady=10, sticky="w")
    personal_number_label = tk.Label(sign_up_window, text="Personal Number:", bg="#B6B6B6")
    personal_number_label.grid(column=0, row=4, padx=10, pady=10, sticky="e")

    # Join Date
    join_date_entry = tk.Entry(sign_up_window)  # we should change join date in future
    join_date_entry.grid(column=1, row=5, padx=10, pady=10, sticky="w")
    join_date_label = tk.Label(sign_up_window, text="Join Date:", bg="#B6B6B6")
    join_date_label.grid(column=0, row=5, padx=10, pady=10, sticky="e")

    # Password
    user_password_entry = tk.Entry(sign_up_window, show="*")
    user_password_entry.grid(column=1, row=6, padx=10, pady=10, sticky="w")
    password_label = tk.Label(sign_up_window, text="Password:", bg="#B6B6B6")
    password_label.grid(column=0, row=6, padx=10, pady=10, sticky="e")

    # Sign Up button
    signup_button = tk.Button(sign_up_window, text="Sign Up", command=sign_up_user)
    signup_button.grid(column=1, row=7, pady=20)

    # back to login button
    back_button = tk.Button(sign_up_window, text= "Back to Login", command = back_to_login)
    back_button.grid(column=0, row=7, pady=20)

def back_to_login():
        sign_up_window.destroy()   # destroys/closes the sign up window
        login_window.deiconify()

def load_window(previous_window):

    global sign_up_window, login_window

    login_window = previous_window # stores the login window in the background so it can be reopennd
    sign_up_window = tk.Toplevel(login_window) # Creates the sign up window on top of the login window

    sign_up_window.title('Bankino')
    sign_up_window.geometry('600x400')
    sign_up_window.configure(bg="#B6B6B6")
    
    ROWS, COLUMNS = 8, 3
    for i in range(COLUMNS):
        sign_up_window.columnconfigure(i, weight=1)
    for i in range(ROWS):
        sign_up_window.rowconfigure(i, weight=1)
    
    header_font = tkFont.Font(family="Times", size=25, weight="bold")
    header = tk.Label(sign_up_window, text="Bankino", bg="#B6B6B6", font=header_font)
    header.grid(column=1, row=0, sticky=tk.NSEW, pady=10)
     
    display_signup()   
