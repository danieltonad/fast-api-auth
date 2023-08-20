from fastapi import FastAPI, Request

async def custom_middleware(request: Request, call_next):
    print('before Req')
    response = await call_next(request)
    print('After Req')
    return response