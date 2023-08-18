import jwt
from dotenv import load_dotenv
import os
from time import time

load_dotenv()

JWT_SECRET = os.environ.get('JWT_SECRET')
JWT_ALGORITHM = os.environ.get('JWT_ALGORITHM')

print(JWT_ALGORITHM)
def token_response(token: str):
    return {
        'access_token': token
    }

def signJWT(userID: str):
    payload = {
        'userID': userID,
        'expiry': time() + 1200
    }
    token = jwt.encode(payload, JWT_SECRET, JWT_ALGORITHM)
    return token_response(token)