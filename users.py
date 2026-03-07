users = {}

def register(username, password):
    if username in users:
        return False
    users[username] = {
        "password": password,
        "history": []
    }
    return True

def login(username, password):
    if username in users and users[username]["password"] == password:
        return True
    return False

def add_history(username, query):
    if username in users:
        users[username]["history"].append(query)

def get_history(username):
    if username in users:
        return users[username]["history"]
    return []