from fastapi import APIRouter
from request.create_user_request import createUserRequest
from auth.jwt import signJWT, decodeJWT

user = APIRouter()


@user.post('/add_user', tags=['User Registrartion'])
def save_user(user: createUserRequest):
    user = dict(user)
    return decodeJWT(signJWT(user)['access_token'])