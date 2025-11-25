import pages.login_window
import pages.landing_page


#call pages.window_name.load_window() for each window you want to load. REMEMBER that you CAN pass variables to your load_window()-function if needed

def main():
    pages.login_window.load_window()

    # Based on the info inputted in the login window, we try to login the user and navigate to their landing page. 
    logged_in_user = ""
    try:
        with open ("./data/cache/logged_in_user.cache", "r") as file:
            logged_in_user = file.read()
            if logged_in_user == "":
                print("Unable to navigate to landing page because user is not logged in")
            else:
                print("logged in user is : " + logged_in_user)
                pages.landing_page.load_window(logged_in_user)
    except FileNotFoundError:
        print("File not found")

if __name__ == "__main__":
    main()