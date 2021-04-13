import database_manipulate


def admin_main():
    while True:
        print("Введите SQL запрос. Для выхода введите 0")
        key = input()
        if key == "0":
            break
        else:
            database_manipulate.SQL_input(key)
