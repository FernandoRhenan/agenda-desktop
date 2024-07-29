import sqlite3
import os


def initDatabase():

    path = os.path.abspath("./database.db")
    with sqlite3.connect(path) as connection:
        cursor = connection.cursor()
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS schedule(name TEXT NOT NULL, service TEXT NOT NULL, data TEXT UNIQUE, time TEXT UNIQUE, PRIMARY KEY (data, time));")
        connection.commit()


def commitQuery(q, values):
    path = os.path.abspath("./database.db")
    with sqlite3.connect(path) as connection:
        cursor = connection.cursor()
        cursor.execute(q, (values))
        connection.commit()


def query(q):
    path = os.path.abspath("./database.db")
    with sqlite3.connect(path) as connection:
        cursor = connection.cursor()
        res = cursor.execute(q)
        return res.fetchall()
