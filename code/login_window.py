import tkinter as tk
import tkinter.font as tkFont
import password_checker

def login_user():
    saved_info = dict()
    saved_info['personal_number'] = personal_number.get()
    saved_info['password'] = user_password.get()
    print(saved_info)

    hashed_password = password_checker.hash_password(saved_info["password"])

    if password_checker.verify_user(int(saved_info["personal_number"]), hashed_password):
        print("Login successful.")
        return True
    else:
        print("Invalid credentials.")
        return False


def display_login():
    personal_number_label = tk.Label(root, text="Personal Number:", bg="#B6B6B6")
    personal_number_label.grid(column=0, row=1, padx=10, pady=10, sticky="e")

    global personal_number
    global user_password

    personal_number = tk.Entry(root)
    personal_number.grid(column=1, row=1, padx=10, pady=10, sticky="w")

    # Password
    password_label = tk.Label(root, text="Password:", bg="#B6B6B6")
    password_label.grid(column=0, row=2, padx=10, pady=10, sticky="e")

    user_password = tk.Entry(root, show="*")
    user_password.grid(column=1, row=2, padx=10, pady=10, sticky="w")

    # Login button
    login_button = tk.Button(root, text="Login", command =login_user)
    login_button.grid(column=1, row=3, pady=20)

def main():
    global root
    root = tk.Tk()  # Creates the window
    root.title('Bankino')
    root.geometry('600x400')
    root.configure(bg="#B6B6B6")

    ROWS = 5
    COLUMNS = 3

    for i in range(COLUMNS):
        root.columnconfigure(i, weight=1)
    for i in range(ROWS):
        root.rowconfigure(i, weight=1)


    header_font = tkFont.Font(family="Times", size=25, weight="bold")

    header = tk.Label(root, text="Bankino", bg="#B6B6B6", font=header_font)
    header.grid(column=1, row=0, sticky=tk.NSEW, pady=10)

    display_login()


if __name__ == "__main__":
    main()

tk.mainloop()
