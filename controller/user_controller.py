from request.user_request import createUserRequest, userLoginRequest, passwordChangeRequest
import uuid
from pydantic import EmailStr
from config.db import database
from schema.user_schema import users_serializer, user_serializer
from utility.hash import hash_pwd
from auth.jwt import signJWT
from model.user_model import UserModel

def login_user(user: userLoginRequest):
    try:
        # print(database.fetch({'email': user.email}, limit=1)._items[0])
        find = user_serializer(database.fetch({'email': user.email}, limit=1)._items[0])
        if find['password'] == hash_pwd(user.password):
            return signJWT(find)
        return {'details': 'invalid user credentials'}
    except:
        return {'details': 'Network Error'}


def create_user(user: createUserRequest):
    if not checkEmailDuplicate(user.email):
        key = str(uuid.uuid1())
        user.password =  hash_pwd(user.password)
        user_obj = {'key': key}
        user_obj.update(user)
        return 'User Created' if database.put(user_obj) else 'Unable to create user !!'
    else:
        return {'details': 'Email Already Exist!'}

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

def password_change(user: UserModel, payload):
    if user['password'] == hash_pwd(payload['old_password']):
         if payload['old_password'] != payload['new_password']:
             user['password'] = hash_pwd(payload['new_password'])
             change = database.update(updates={'password': hash_pwd(payload['new_password'])}, key=user['id'])
             print(change)
             return {'details': 'password changed'} if not change else {'details': 'unable to change password '}
         else:
             return {'details': 'old password cannot be same as new'}
    else:
        return {'details': 'incorrect password'}