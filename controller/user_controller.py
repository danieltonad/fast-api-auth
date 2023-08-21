from request.create_user_request import createUserRequest
import uuid
from pydantic import EmailStr
from config.db import database

def create_user(user: createUserRequest):
    id = str(uuid.uuid1())
    user_obj = 
    print(user)
    return 100

def checkEmailDuplicate(email: EmailStr):
    users = database

def getUsers() -> []:
    dat