from fastapi import FastAPI
from request.user_request import createUserRequest
from auth.jwt import signJWT, decodeJWT
from middleware.auth import custom_middleware
from routes.user import user
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all HTTP headers
)

app.include_router(user, prefix='/user')

app.middleware('http')(custom_middleware)
