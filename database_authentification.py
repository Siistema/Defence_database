import database_connect


def database_auth(login, passwd):
    connection, cur = database_connect.connect_database()
    ban_word = ["#", "'", '"']
    query = ("SELECT * FROM `users` WHERE name=" + login + " and passwd=" + passwd)
    #  print(query)

    for word in ban_word:
        if (query.find(word) != -1):
            exit("SQL INJECTION ERROR")
    login = "'" + login + "'"
    passwd = "'" + passwd + "'"
    query = ("SELECT * FROM `users` WHERE name=" + login + " and passwd=" + passwd)
    cur.execute(query)
    data = cur.fetchall()
    connection.commit()
    cur.close()
    connection.close()

    if (len(data) == 0):
        return 0, None
    else:
        return data[0][2], data[0][3]
