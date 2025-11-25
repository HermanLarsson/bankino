import pages.login_window


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