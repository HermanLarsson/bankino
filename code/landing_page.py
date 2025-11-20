import tkinter as tk
import tkinter.font as tkFont
import json

logged_in_id = "4XJ38"
bank_accounts = {}
account_headers = []
account_amounts = []

root = tk.Tk() #Creates the window
root.title('Bankino')
root.geometry('1000x1000')
#root.configure(bg = "#B6B6B6") #Configures the background


ROWS = 20
COLUMNS = 20

#Configures the amount of columns and rows
for i in range(COLUMNS):
    root.columnconfigure(i, weight = 1)
for i in range(ROWS):
    root.rowconfigure(i, weight = 1)


header_font = tkFont.Font(family = "Calibri", size = 25, weight = "bold")
value_font = tkFont.Font(family = "Courier", size = 15, weight = "normal")

#Creates the header as a Label over the entire cell
header = tk.Label(root, text = "Bankino", font = header_font)
header.grid(column=0, row=0, sticky=tk.NSEW)

#Loads the users bank accounts. 
def load_bank_accounts():
    f = open("./data/bank_accounts/accounts.json")
    data = json.load(f)
    f.close()
    if logged_in_id in data.keys():
        for account in data[logged_in_id].items():
            bank_accounts[account[0]] = account[1] 



load_bank_accounts()

account_counter = 0
for account in bank_accounts.items():
    account_headers.append(tk.Label(root, text = (account[0]), font = header_font))
    account_amounts.append(tk.Label(root, text = (str(account[1]["balance"]) + " SEK"), font = value_font))
    account_amounts[account_counter].grid(column = 3, row = account_counter + 2)
    account_headers[account_counter].grid(column = 0, row = account_counter + 2)
    account_counter += 1

root.mainloop() #Main functions which runs the program






def main():
    print("Done")




if __name__ == "__main__":
    main()