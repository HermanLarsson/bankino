import tkinter.font as tkFont

def initialize_fonts():

    # Regular Fonts
    global body_font
    global header_font
    global header2_font
    global value_font
    global button_font
    global nav_font

    body_font = tkFont.Font(family="Calibri", size = 20, weight = "bold")
    header_font = tkFont.Font(family = "Calibri", size = 30, weight = "bold")
    header2_font = tkFont.Font(family="Calibri", size = 25, weight = "bold")
    value_font = tkFont.Font(family = "Courier", size = 15, weight = "normal")
    button_font = tkFont.Font(family="Calibri", size = 12, weight = "normal")
    nav_font = tkFont.Font(family = "Calibri", size = 13, weight = "bold")


    # Card Fonts
    global smaller_text_font
    global smaller_num_font
    global normal_text_font
    global normal_num_font

    smaller_text_font = tkFont.Font(family="Calibri", size = 20, weight = "normal")
    smaller_num_font = tkFont.Font(family="Calibri", size = 35, weight = "normal")
    normal_text_font = tkFont.Font(family="Calibri", size = 40, weight = "bold")
    normal_num_font = tkFont.Font(family="Calibri", size = 60, weight = "normal")

