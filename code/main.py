import pages.login_window
import os
import fonts.bankino_fonts as fonts


def reset_cache():
    try:
        with open ("./data/cache/logged_in_user.cache", "w") as file:
            file.write("")
    except:
        os.makedirs("./data/cache")
        with open ("./data/cache/logged_in_user.cache", "w") as file:
            file.write("")


#call pages.window_name.load_window() for each window you want to load. REMEMBER that you CAN pass variables to your load_window()-function if needed

def main():
    reset_cache()
    
    login_window = pages.login_window.load_window()
    login_window.mainloop()

if __name__ == "__main__":
    main()