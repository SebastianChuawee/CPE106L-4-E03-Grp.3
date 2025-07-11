# data_access.py

def load_users(filename="user.txt"):
    users = {}
    try:
        with open(filename, "r") as file:
            for line in file:
                username, password = line.strip().split(",")
                users[username] = password
    except FileNotFoundError:
        print("user.txt not found.")
    return users

def save_user(username, password, filename="user.txt"):
    with open(filename, "a") as file:
        file.write(f"{username},{password}\n")
