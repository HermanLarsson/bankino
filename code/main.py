import pages.login_window
import os
import fonts.bankino_fonts as fonts
import backend.db_queries as db_queries
from pages.login_window import LoginWindow

#call pages.window_name.load_window() for each window you want to load. REMEMBER that you CAN pass variables to your load_window()-function if needed

def main():
    db_queries.reset_cache()

    app = LoginWindow()
    fonts.initialize_fonts()
    app.mainloop()

if __name__ == "__main__":
    main()