from fastapi import APIRouter, Header, Depends, Request
from request.create_user_request import createUserRequest, userLoginRequest
from controller.user_controller import create_user, login_user
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
async def user_dashboard(token: Annotated[decodeJWT, Depends()]):
    # print(request.headers.keys())
    return token