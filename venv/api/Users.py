from flask import Flask, g, session
from passlib.apps import custom_app_context as pwd_context
from DB_Access import add_user, search_user


def create_new_user(user_name, password):
    if search_user(user_name, hash_password(password)):
        print 'user already exists'
        return False
    add_user(user_name, password)
    connect_user(user_name)
    return True


def verify_user(user_name, password):
    if search_user(user_name, hash_password(password)):
        connect_user(user_name)
        return True
    return False


def hash_password(password):
    return password


def connect_user(user_name):
    """this connects a user. DO NOT use this without varefiying the user first."""
    session['username'] = user_name
    session['logged_in'] = True
