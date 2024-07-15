import sqlite3


def initDatabase():
    with sqlite3.connect("./src/infra/agenda_database.db") as connection:
        cursor = connection.cursor()
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS teste(umacoluna text, duascolunas integer);")
        connection.commit()


def commitQuery(q):
    with sqlite3.connect("./src/infra/agenda_database.db") as connection:
        cursor = connection.cursor()
        cursor.execute(q)
        connection.commit()


def query(q):
    with sqlite3.connect("./src/infra/agenda_database.db") as connection:
        cursor = connection.cursor()
        res = cursor.execute(q)
        return res.fetchall()