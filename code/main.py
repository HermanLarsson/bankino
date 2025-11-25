import pages.login_window


#call pages.window_name.load_window() for each window you want to load. REMEMBER that you CAN pass variables to your load_window()-function if needed

def main():
    pages.login_window.load_window()
    logged_in_user = ""
    try:
        with open ("./data/cache/logged_in_user.cache", "r") as file:
            logged_in_user = file.read()
    except FileNotFoundError:
        print("File not found")

    print(logged_in_user)



if __name__ == "__main__":
    main()