from fastapi import APIRouter
from request.create_user_request import createUserRequest, userLoginRequest
from controller.user_controller import create_user, login_user

user = APIRouter()


@user.post('/register', tags=['User Registrartion'])
def save_user(user: createUserRequest):
    return create_user(user)

@user.post('/login', tags=['User Login'])
def user_login(user: userLoginRequest):
    return login_user(user)