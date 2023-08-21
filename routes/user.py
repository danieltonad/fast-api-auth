from fastapi import APIRouter, Header, Depends, Request
from request.user_request import createUserRequest, userLoginRequest, passwordChangeRequest
from controller.user_controller import create_user, login_user, password_change
from typing import Annotated
from model.user_model import UserModel
from auth.jwt import decodeJWT

user = APIRouter()


@user.post('/register', tags=['User Registrartion'])
def save_user(user: createUserRequest):
    return create_user(user)

@user.post('/login', tags=['User Login'])
def user_login(user: userLoginRequest):
    return login_user(user)

@user.get('/dashboard', tags=['Dashboard'])
async def user_dashboard(user: Annotated[decodeJWT, Depends()]):
    return user

@user.post('/change_password', tags=['Change Password'])
async def user_change_password(payload: passwordChangeRequest ,user: Annotated[decodeJWT, Depends()]):
    return password_change(user, dict(payload))
