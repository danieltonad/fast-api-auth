from fastapi import  Request
from auth.jwt import decodeJWT

async def custom_middleware(request: Request, call_next):
    path = request.url.path.startswith('/user/dashboard')
    print(path)
    if path:
        print(request.headers.keys())
    response = await call_next(request)
    
    return response