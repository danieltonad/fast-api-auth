from pydantic import BaseModel, EmailStr


class createUserRequest(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    password: str