from pydantic import BaseModel, EmailStr
from typing import Literal

class UserBase(BaseModel):
    email: EmailStr
    tipo: Literal['empresa', 'freelancer']

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int
    is_active: bool

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str
