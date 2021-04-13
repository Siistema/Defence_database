import mysql.connector
from mysql.connector import Error


def connect_database():
    servername_DB = "127.0.0.1"
    username_DB = "root"
    password_DB = "123456"
    dbname_DB = "test"
    connection_DB = create_connection(servername_DB, username_DB, password_DB, dbname_DB)
    cursor = connection_DB.cursor()
    return (connection_DB, cursor)


def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )

    except Error as e:
        print("The error '{e}' occurred")
    return connection
