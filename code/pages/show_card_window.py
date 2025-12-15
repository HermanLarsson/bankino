from tkinter import *
import os
import backend.db_queries as db_queries
import tkinter.font as tkFont


IMAGES_PATH = os.path.abspath(os.path.join(db_queries.BASE_DIR, "..", "..", "data", "images"))
CARDS_PATH = os.path.abspath(os.path.join(db_queries.BASE_DIR, "..", "..", "data", "account_cards", "cards.json"))


def load_window(parent, user_id, card_number):

    smaller_font = tkFont.Font(family="Calibri", size = 20, weight = "normal")
    small_font = tkFont.Font(family="Calibri", size = 35, weight = "normal")
    medium_font = tkFont.Font(family="Calibri", size = 40, weight = "bold")
    big_font = tkFont.Font(family="Calibri", size = 60, weight = "normal")

    global show_card_window
    show_card_window = Toplevel(parent)
    show_card_window.resizable(width=False, height=False)
    show_card_window.title('Bankino')
    show_card_window.geometry('1004x634') #Exact dimensions of the card
    card_image = PhotoImage(file =  os.path.join(IMAGES_PATH, "template_card.png")) #Saves the image in a variable

    #Configures the amount of columns and rows
    ROWS = 20
    COLUMNS = 20
    for i in range(COLUMNS):
        show_card_window.columnconfigure(i, weight=1)
    for i in range(ROWS):
        show_card_window.rowconfigure(i, weight=1)

    all_cards = db_queries.get_cards()
    curr_acccount_card  = all_cards[user_id][card_number]
    formatted_car_num = format_card_num(card_number)

    #Creates a label and places it over the entire window
    background_label = Label(show_card_window, image=card_image) 
    background_label.place(x=0, y=0)

    #Creates and display labels of the card info
    card_number_label = Label(show_card_window, text=formatted_car_num, bg="#15150e", fg="#FFDD43", font=big_font)
    card_number_label.grid(column=5, row=10, sticky="nw", columnspan=5)
    
    last_name_label = Label(show_card_window, text=curr_acccount_card["cardholder_last_name"], bg="#15150e", fg="#FFDD43", font=medium_font)
    last_name_label.grid(column=5, row=11, sticky="sw", padx=20)

    first_name_label = Label(show_card_window, text=curr_acccount_card["cardholder_first_name"], bg="#15150e", fg="#FFDD43", font=medium_font)
    first_name_label.grid(column=5, row=12, sticky="nw", padx=20)

    come_up_with_name = Label(show_card_window, text="Valid thru:", bg="#15150e", fg="#FFDD43", font=smaller_font)
    come_up_with_name.grid(column=6, row=12, sticky="ne", padx=5, pady=5)

    expiration_date_label = Label(show_card_window, text=curr_acccount_card["expiration_date"], bg="#15150e", fg="#FFDD43", font=small_font)
    expiration_date_label.grid(column=7, row=12, sticky="nw")

    come_up_with_name2 = Label(show_card_window, text="CVC:", bg="#15150e", fg="#FFDD43", font=smaller_font)
    come_up_with_name2.grid(column=8, row=12, sticky="ne", padx=5, pady=5)

    security_code_label = Label(show_card_window, text=curr_acccount_card["security_code"], bg="#15150e", fg="#FFDD43", font=small_font)
    security_code_label.grid(column=9, row=12, sticky="nw")

    parent.mainloop()


#Formats the card number to look nicer
def format_card_num(card_num):
    format_card_num = ""
    previous_index = 0
    for i in range(0, len(card_num) + 1, 4):
        format_card_num += card_num[previous_index : i] + " "
        previous_index = i

    return format_card_num


