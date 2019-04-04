from werkzeug.security import safe_str_cmp
from user import User


def pp(n):
    print()
    print(n)

users = [
    User(1, 'Alucard', 'Qwertyui'),
    User(2, 'Alucard2', 'Qwertyui'),
]


username_table = {u.username: u for u in users}
userid_table = {u.id: u for u in users}


def authenticate(username, password):
    user = username_table.get(username, None)
    if user and safe_str_cmp(user.password.encode('utf-8'), password.encode('utf-8')):
        return user

def identity(payload):
    user_id = payload['identity']
    return userid_table.get(user_id, None)






