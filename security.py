from werkzeug.security import safe_str_cmp

from Model.Users import UserModal


def authenticate(username, password):
    user = UserModal.find_by_username(username)
    print(user)
    if user and safe_str_cmp(user.password, password):
        print('check passed')
        return user


def identity(payload):
    print(payload)
    user_id = payload['identity']
    return UserModal.find_by_id(user_id)
       