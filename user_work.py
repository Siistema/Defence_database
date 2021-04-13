import database_manipulate


def user_main():
    while True:
        print("Нажмите соответсвующую цифру:\n(1): Вывод таблицы\n(2): Выход")
        key = input()
        if int(key) == 1:
            print("tablica")
            sql_select_table()
        elif int(key) == 2:
            break
        else:
            print("INPUT ERROR")


def sql_select_table():
    while True:
        print("Выберите таблицу, которую необходимо вывести:\n(1): Users\n(2): Price\n(3): Назад")
        key = input()
        if int(key) == 1:
            database_manipulate.database_select("users")
        elif int(key) == 2:
            database_manipulate.database_select("price")
        elif int(key) == 3:
            break
        else:
            print("input error")
