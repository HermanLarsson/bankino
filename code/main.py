import fonts.bankino_fonts as fonts
import backend.db_queries as db_queries
from pages.login_window import LoginWindow
from pages.landing_page import LandingPageWindow

def main():
    db_queries.reset_cache()
    program_state = "logged_out"
    while(program_state != 'closed'):
        program_state = db_queries.check_program_state()
        app = None
        if program_state == 'logged_out':
            app = LoginWindow()
            fonts.initialize_fonts()
            app.mainloop()
        elif program_state == 'logged_in':
            app = LandingPageWindow(db_queries.get_logged_in_user())
            app.mainloop()

if __name__ == "__main__":
    main()