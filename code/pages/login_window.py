import tkinter as tk
import tkinter.font as tkFont
import backend.password_checker as password_checker
import pages.landing_page as landing_page


# Login user will save the user_id in cache-file and destroy the window if successful
# If login fails, nothing will happen
def login_user():
    saved_info = dict()
    saved_info['personal_number'] = personal_number.get()
    saved_info['password'] = user_password.get()
    print(saved_info)

    hashed_password = password_checker.hash_password(saved_info["password"])

    login_check = password_checker.verify_user(int(saved_info["personal_number"]), hashed_password)
    if login_check == "":
        print("Invalid credentials.")
        try:
            with open ("./data/cache/logged_in_user.cache", "w") as file:
                file.write(login_check)
        except FileNotFoundError:
            print("File not found")
    else:
        print("Login successful.")
        try:
            with open ("./data/cache/logged_in_user.cache", "w") as file:
                file.write(login_check)
        except FileNotFoundError:
            print("File not found")
        login_window.destroy()
        


def display_login():
    personal_number_label = tk.Label(login_window, text="Personal Number:", bg="#B6B6B6")
    personal_number_label.grid(column=0, row=1, padx=10, pady=10, sticky="e")

    global personal_number
    global user_password

    personal_number = tk.Entry(login_window)
    personal_number.grid(column=1, row=1, padx=10, pady=10, sticky="w")

    # Password
    password_label = tk.Label(login_window, text="Password:", bg="#B6B6B6")
    password_label.grid(column=0, row=2, padx=10, pady=10, sticky="e")

    user_password = tk.Entry(login_window, show="*")
    user_password.grid(column=1, row=2, padx=10, pady=10, sticky="w")

    # Login button
    login_button = tk.Button(login_window, text="Login", command =login_user)
    login_button.grid(column=1, row=3, pady=20)

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

    display_login()
    tk.mainloop()
