from pydantic import BaseModel, EmailStr
 
class user(BaseModel):
    id: str
    first_name: str
    last_name: str
    email: EmailStr
    password: str
    active: bool