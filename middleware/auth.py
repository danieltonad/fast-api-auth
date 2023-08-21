from fastapi import  Request
from auth.jwt import decodeJWT

async def custom_middleware(request: Request, call_next):
    path = request.url.path
    # print(f'body->{request.path_params}')
    # _ = await request.json()
    response = await call_next(request)
    print('After Req')
    # print(f'body->{await request.json()}')
    return response