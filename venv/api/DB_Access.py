import sqlite3
import datetime
from flask import session, g
from utils import sql_row_to_dict


def search_entry(id):
    """Search entry by id. Returns a dict with all entry information"""
    query = "SELECT * FROM posts WHERE id = :id"
    c = g.db.execute(query, {'id': str(id)})
    row = c.fetchone()
    if row is None:
        return False
    return sql_row_to_dict(c, row)


def add_entry(entryRequest):
    """Add an enrty into the DB."""

    query = '''INSERT INTO posts(content, creation_date, creator_username, upvotes, downvotes) 
    VALUES(:content, :creation_date, :creator_username, 0, 0)'''#content, creation date, and username are given within the request. up/down votes get defult value of 0.

    parameters = {'content': entryRequest['content'],
                  'creation_date': str(datetime.datetime.now),
                  'creator_username': session['username']}

    g.db.execute(query, parameters)
    g.db.commit()

    return True


def delete_entry(id):
    #ToDo: delete the etry at id
    pass


def add_user(user_name, password):
    query = '''
    INSERT INTO users(username, password) 
        VALUES(:name, :password)'''

    parameters = {'name': user_name, 'password': password}

    g.db.execute(query, parameters)
    g.db.commit()


def search_user(username, password):
    query = '''SELECT username FROM users WHERE username = :name AND password = :password'''
    parameters = {'name': username, 'password': password}

    c = g.db.execute(query, parameters)
    if c.fetchone() is None:
        return False
    return True
