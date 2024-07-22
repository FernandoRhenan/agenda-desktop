import sqlite3


def initDatabase():
    with sqlite3.connect("./src/infra/agenda_database.db") as connection:
        cursor = connection.cursor()
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS schedule(name TEXT NOT NULL, service TEXT NOT NULL, data TEXT UNIQUE, time TEXT UNIQUE, PRIMARY KEY (data, time));")
        connection.commit()


def commitQuery(q, values):
    with sqlite3.connect("./src/infra/agenda_database.db") as connection:
        cursor = connection.cursor()
        cursor.execute(q, (values))
        connection.commit()


def query(q):
    with sqlite3.connect("./src/infra/agenda_database.db") as connection:
        cursor = connection.cursor()
        res = cursor.execute(q)
        return res.fetchall()
