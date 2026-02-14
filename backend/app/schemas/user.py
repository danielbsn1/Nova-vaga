from pydantic import BaseModel, EmailStr
from typing import Literal


class UserBase(BaseModel):
    email: EmailStr
    tipo: Literal["empresa", "freelancer"]


class UserCreate(UserBase):
    password: str


class LoginSchema(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str