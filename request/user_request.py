from pydantic import BaseModel, EmailStr


class createUserRequest(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    password: str

class userLoginRequest(BaseModel):
    email: EmailStr
    password: str

class passwordChangeRequest(BaseModel):
    old_password: str
    new_password: str