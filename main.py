from fastapi import FastAPI
from request.create_user_request import createUserRequest
from auth.jwt import signJWT, decodeJWT
from middleware.auth import custom_middleware
from routes.user import user
import hashlib

app = FastAPI()

app.include_router(user, prefix='/user')

app.middleware('http')(custom_middleware)
