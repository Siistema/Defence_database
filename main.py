import database_authentification
import generate_google_code
import user_work
import admin_work


def main():
    login = input("Enter login: ")
    passwd = input("Enter password: ")
    permission, google_code = database_authentification.database_auth(login, passwd)
    if permission == "admin":
        print("You admin")
        code = input("Enter google code: ")
        if generate_google_code.google_auth(code, google_code):
            admin_work.admin_main()
        else:
            exit("Google key error")
    elif permission == "user":
        print("You user")
        code = input("Enter google code: ")
        if generate_google_code.google_auth(code, google_code):
            user_work.user_main()
        else:
            exit("Google key error")
    else:
        print("auth error")


if __name__ == '__main__':
    main()
