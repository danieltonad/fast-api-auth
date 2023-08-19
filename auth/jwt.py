import jwt
from fastapi import HTTPException, Header
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

def signJWT(user: str):
    payload = {
        'user': user,
        'expiry': time() + 1200
    }
    token = jwt.encode(payload, JWT_SECRET, JWT_ALGORITHM)
    return token_response(token)

def decodeJWT(token: str):
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, JWT_ALGORITHM)
        print(decoded_token)
        # if decoded_token:
        #     def getUser():
        #         return decoded_token['user']
        return True
        # return True if decoded_token['expires'] >= time() else HTTPException(status_code=401, detail="Unathorized")

    except:
        return HTTPException(status_code=500, detail="Token Error", headers=Header())
