from pydantic import BaseModel, EmailStr
 
class UserModel(BaseModel):
    id: str
    first_name: str
    last_name: str
    email: EmailStr
    password: str