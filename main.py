from fastapi import FastAPI
from request.create_user_request import createUserRequest
from auth.jwt import signJWT
app = FastAPI()


@app.post('/add_user', tags=['User Registrartion'])
def save_user(user: createUserRequest):
    user = dict(user)
    
    return signJWT('a0rCC7kmhPUM_Ytmy34EmXSZnLoqr3XuBjphgxi6LL2rC')