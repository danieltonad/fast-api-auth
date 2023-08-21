from fastapi import APIRouter
from request.create_user_request import createUserRequest
from controller.user_controller import create_user
from auth.jwt import signJWT, decodeJWT

user = APIRouter()


@user.post('/add_user', tags=['User Registrartion'])
def save_user(user: createUserRequest):
    return create_user(user)