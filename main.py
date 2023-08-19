from fastapi import FastAPI
from request.create_user_request import createUserRequest
from auth.jwt import signJWT, decodeJWT
app = FastAPI()


@app.post('/add_user', tags=['User Registrartion'])
def save_user(user: createUserRequest):
    user = dict(user)
    return decodeJWT(signJWT('100'))