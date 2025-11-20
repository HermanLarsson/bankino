import tkinter as tk
import tkinter.font as tkFont


root = tk.Tk() #Creates the window
root.title('Bankino')
root.geometry('600x400')
root.configure(bg = "#B6B6B6") #Configures the background


ROWS = 5
COLUMNS = 3

#Configures the amount of columns and rows
for i in range(COLUMNS):
    root.columnconfigure(i, weight = 1)
for i in range(ROWS):
    root.rowconfigure(i, weight = 1)


header_font = tkFont.Font(family = "Times", size = 25, weight = "bold")

#Creates the header as a Label over the entire cell
header = tk.Label(root, text = "Bankino", bg = "#B6B6B6", font = header_font)
header.grid(column=1, row=0, sticky=tk.NSEW)


root.mainloop() #Main functions which runs the program