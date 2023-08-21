import jwt
from fastapi import HTTPException
from dotenv import load_dotenv
import os
from time import time

load_dotenv()

JWT_SECRET = os.environ.get('JWT_SECRET')
JWT_ALGORITHM = os.environ.get('JWT_ALGORITHM')

def token_response(token: str):
    return {
        'access_token': token
    }

def signJWT(user: dict):
    payload = {
        'user': user,
        'expiry': time() + 1200
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token_response(token)

def decodeJWT(token: str):
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        # print(decoded_token)
        return decoded_token['user'] if  decoded_token['expiry'] >= time() else HTTPException(status_code=401, detail="authorization expired")

    except:
        raise HTTPException(status_code=401, detail="UnAuthorized")
