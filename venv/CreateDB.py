import sqlite3
from sqlite3 import Error


def AddTableToDB(conn):

    create_users = '''CREATE TABLE IF NOT EXISTS users (id integer PRIMARY KEY, username text NOT NULL, password text);'''

    create_posts = '''CREATE TABLE IF NOT EXISTS posts (
    id integer PRIMARY KEY,
    content text NOT NULL,
    creation_date text NOT NULL,
    creator_username text NOT NULL,
    upvotes integer NOT NULL,
    downvotes integer NOT NULL);'''

    try:
        c = conn.cursor()
        c.execute(create_users)
        c.execute(create_posts)
    except Error as e:
        print(e)

def createDB(path):
    """ create a database connection to a SQLite database """
    try:
        conn = sqlite3.connect(path)

        AddTableToDB(conn)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        conn.close()


createDB(r"C:\Users\User\Desktop\Microblog-Project\Microblog-Pendo-Task\venv\Database.db")