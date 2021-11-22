import sqlite3 as sql
from os import path

ROOT = path.dirname(path.relpath(__file__))

def create_history(history):
    con = sql.connect(path.join(ROOT, 'database.db'))
    cur = con.cursor()
    cur.execute('INSERT INTO HISTORY values (?)', (history, ))
    con.commit()
    con.close()

def get_history():
    con = sql.connect(path.join(ROOT, 'database.db'))
    cur = con.cursor()
    cur.execute('SELECT * FROM HISTORY')
    history = cur.fetchall()
    return history
