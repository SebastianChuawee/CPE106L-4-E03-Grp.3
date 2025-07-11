# auth_logic.py

from data_access import load_users, save_user

def authenticate(username, password):
    users = load_users()
    return username in users and users[username] == password

def register_user(username, password):
    users = load_users()
    if username in users:
        return False
    save_user(username, password)
    return True
