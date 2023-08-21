from request.create_user_request import createUserRequest
import uuid
from pydantic import EmailStr
from config.db import database
from schema.user_schema import users_serializer
from utility.hash import hash_pwd

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
    users = getUsers()
    if users:
        for _ in users:
            if _['email'] == email:
                return True
    return False

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