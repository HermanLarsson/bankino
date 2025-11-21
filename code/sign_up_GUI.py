import tkinter as tk
import tkinter.font as tkFont
import sign_up





def sign_up_user():
    # get inputs
    first_name_input = first_name_entry.get()
    last_name_input = last_name_entry.get()
    middle_name_input = middle_name_entry.get()
    personal_number_input = personal_number_entry.get()
    join_date_input = join_date_entry.get()
    password_input = user_password_entry.get()






    # Call the sign up function
    sign_up.sign_up(first_name_input, last_name_input, middle_name_input,
                    personal_number_input, join_date_input, password_input)
    
  



def display_signup():
    global first_name_entry, last_name_entry, middle_name_entry
    global personal_number_entry, join_date_entry, user_password_entry

   
    
    
    first_name_entry = tk.Entry(root)
    last_name_entry = tk.Entry(root)
    middle_name_entry = tk.Entry(root)
    personal_number_entry = tk.Entry(root)
    join_date_entry = tk.Entry(root)
    user_password_entry = tk.Entry(root, show="*")
    


    # First Name
    first_name_entry = tk.Entry(root)
    first_name_entry.grid(column=1, row=1, padx=10, pady=10, sticky="w")
    first_name_label = tk.Label(root, text="First Name:", bg="#B6B6B6")
    first_name_label.grid(column=0, row=1, padx=10, pady=10, sticky="e")




    # Last Name
    last_name_entry = tk.Entry(root)
    last_name_entry.grid(column=1, row=2, padx=10, pady=10, sticky="w")
    last_name_label = tk.Label(root, text="Last Name:", bg="#B6B6B6")
    last_name_label.grid(column=0, row=2, padx=10, pady=10, sticky="e")





    # Middle Name
    middle_name_entry = tk.Entry(root)
    middle_name_entry.grid(column=1, row=3, padx=10, pady=10, sticky="w")
    middle_name_label = tk.Label(root, text="Middle Name:", bg="#B6B6B6")
    middle_name_label.grid(column=0, row=3, padx=10, pady=10, sticky="e")






    # Personal Number
    personal_number_entry = tk.Entry(root)
    personal_number_entry.grid(column=1, row=4, padx=10, pady=10, sticky="w")
    personal_number_label = tk.Label(root, text="Personal Number:", bg="#B6B6B6")
    personal_number_label.grid(column=0, row=4, padx=10, pady=10, sticky="e")






    # Join Date
    join_date_entry = tk.Entry(root)
    join_date_entry.grid(column=1, row=5, padx=10, pady=10, sticky="w")
    join_date_label = tk.Label(root, text="Join Date:", bg="#B6B6B6")
    join_date_label.grid(column=0, row=5, padx=10, pady=10, sticky="e")







    # Password
    user_password_entry = tk.Entry(root, show="*")
    user_password_entry.grid(column=1, row=6, padx=10, pady=10, sticky="w")
    password_label = tk.Label(root, text="Password:", bg="#B6B6B6")
    password_label.grid(column=0, row=6, padx=10, pady=10, sticky="e")







    # Sign Up button
    signup_button = tk.Button(root, text="Sign Up", command=sign_up_user)
    signup_button.grid(column=1, row=7, pady=20)










def main():
    global root
    root = tk.Tk() # Creates the window
    root.title('Bankino')
    root.geometry('600x400')
    root.configure(bg="#B6B6B6")
    





    
    ROWS, COLUMNS = 8, 3
    for i in range(COLUMNS):
        root.columnconfigure(i, weight=1)
    for i in range(ROWS):
        root.rowconfigure(i, weight=1)
    
   




    header_font = tkFont.Font(family="Times", size=25, weight="bold")
    header = tk.Label(root, text="Bankino", bg="#B6B6B6", font=header_font)
    header.grid(column=1, row=0, sticky=tk.NSEW, pady=10)
    




    
    
    display_signup()
    
    
    root.mainloop()

if __name__ == "__main__":
    main()
