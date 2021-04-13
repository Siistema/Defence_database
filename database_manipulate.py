import database_connect
from mysql.connector import Error


def SQL_input(request):
    try:
        connection, cur = database_connect.connect_database()
        cur.execute(request)

        data = cur.fetchall()

    except Error as err:
        print(err)
    else:
        print("SUCCESSFUL REQUEST!\nserver answer:\n" + (str)(data))
        # print(data)
        connection.commit()
        cur.close()
        connection.close()


def database_values(table):
    rows = 0
    columns = 0
    connection, cur = database_connect.connect_database()
    query = ("SELECT * FROM " + table)
    cur.execute(query)
    data = cur.fetchall()
    for row in data:
        rows += 1
    for column in data[0]:
        columns += 1
    connection.commit()
    cur.close()
    connection.close()
    return rows, columns


def database_select(table):
    connection, cur = database_connect.connect_database()
    query = ("SELECT * FROM " + table)
    cur.execute(query)
    data = cur.fetchall()
    rows, columns = database_values(table)
    for row in range(0, rows):
        for column in range(0, columns):
            print(data[row][column] + "\t")
        print("\n")
    connection.commit()
    cur.close()
    connection.close()
