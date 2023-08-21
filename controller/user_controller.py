from request.create_user_request import createUserRequest, userLoginRequest
import uuid
from pydantic import EmailStr
from config.db import database
from schema.user_schema import users_serializer, user_serializer
from utility.hash import hash_pwd
from auth.jwt import signJWT

def login_user(user: userLoginRequest):
    find = user_serializer(database.fetch({'email': user.email}, limit=1)._items[0])
    if find['password'] == hash_pwd(user.password):
        return signJWT(find)
    return {'details': 'invalid user credentials'}


def create_user(user: createUserRequest):
    if not checkEmailDuplicate(user.email):
        key = str(uuid.uuid1())
        user.password =  hash_pwd(user.password)
        user_obj = {'key': key}
        user_obj.update(user)
        return 'User Created' if database.put(user_obj) else 'Unable to create user !!'
    else:
        return {'detals': 'Email Already Exist!'}

def checkEmailDuplicate(email: EmailStr):
    _ = database.fetch({'email': email})._items
    return True if len(_) > 0 else False
def getUsers() -> []:
    data = []
    prev = database.fetch()
    data += prev._items
    _last = prev._last
    while _last:
        recent = database.fetch(last=_last)
        print(recent._last, len(data))
        data += recent._items
        _last = recent._last
    return users_serializer(data)

def delete_user(id: str):
    _del = database.delete('id')
    return True if _del else False

def update_user(id: str, user: dict):
    return 'done'