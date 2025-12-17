import tkinter as tk
import os
import backend.db_queries as db_queries
import tkinter.font as tkFont
IMAGES_PATH = os.path.abspath(os.path.join(db_queries.BASE_DIR, "..", "..", "data", "images"))


class ShowCardWindow(tk.Toplevel):
    def __init__(self, parent, user_id, card_number):
        super().__init__(parent)

        self.title('Bankino')
        self.geometry('1004x634') #Exact dimensions of the card
        self.resizable(width=False, height=False)
        self.card_image = tk.PhotoImage(file =  os.path.join(IMAGES_PATH, "template_card.png"))

        # Specific fonts for the card
        self.smaller_text_font = tkFont.Font(family="Calibri", size = 20, weight = "normal")
        self.smaller_num_font = tkFont.Font(family="Calibri", size = 35, weight = "normal")
        self.normal_text_font = tkFont.Font(family="Calibri", size = 40, weight = "bold")
        self.normal_num_font = tkFont.Font(family="Calibri", size = 60, weight = "normal")

        self.grid_layout()

        all_cards = db_queries.get_cards()
        self.curr_acccount_card  = all_cards[user_id][card_number]
        
        self.create_labels(parent, card_number)

    def grid_layout(self):

        ROWS = 20
        COLUMNS = 20
        for i in range(COLUMNS):
            self.columnconfigure(i, weight=1)
        for i in range(ROWS):
            self.rowconfigure(i, weight=1)

    def create_labels(self, parent, card_number):

        #Creates a label and places it over the entire window
        background_label = tk.Label(self, image=self.card_image) 
        background_label.place(x=0, y=0)

        #Creates and display labels of the card info
        card_number_label = tk.Label(self, text=self.format_card_num(card_number), bg="#15150e", fg="#FFDD43", font=self.normal_num_font)
        card_number_label.grid(column=5, row=10, sticky="nw", columnspan=5)

        last_name_label = tk.Label(self, text=self.curr_acccount_card["cardholder_last_name"], bg="#15150e", fg="#FFDD43", font=self.normal_text_font)
        last_name_label.grid(column=5, row=11, sticky="sw", padx=20)

        first_name_label = tk.Label(self, text=self.curr_acccount_card["cardholder_first_name"], bg="#15150e", fg="#FFDD43", font=self.normal_text_font)
        first_name_label.grid(column=5, row=12, sticky="nw", padx=20)

        expiration_date_text_label = tk.Label(self, text="Valid thru:", bg="#15150e", fg="#FFDD43", font=self.smaller_text_font)
        expiration_date_text_label.grid(column=6, row=12, sticky="ne", padx=5, pady=5)

        expiration_date_label = tk.Label(self, text=self.curr_acccount_card["expiration_date"], bg="#15150e", fg="#FFDD43", font=self.smaller_num_font)
        expiration_date_label.grid(column=7, row=12, sticky="nw")

        security_code_text_label = tk.Label(self, text="CVC:", bg="#15150e", fg="#FFDD43", font=self.smaller_text_font)
        security_code_text_label.grid(column=8, row=12, sticky="ne", padx=5, pady=5)

        security_code_label = tk.Label(self, text=self.curr_acccount_card["security_code"], bg="#15150e", fg="#FFDD43", font=self.smaller_num_font)
        security_code_label.grid(column=9, row=12, sticky="nw")

        parent.mainloop()

    #Formats the card number to look nicer
    def format_card_num(self, card_num):
        format_card_num = ""
        previous_index = 0

        for i in range(0, len(card_num) + 1, 4):
            format_card_num += card_num[previous_index : i] + " "
            previous_index = i

        return format_card_num

