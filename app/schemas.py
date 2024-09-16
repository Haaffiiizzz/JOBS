from pydantic import BaseModel, EmailStr
from datetime import datetime


class CreateUser(BaseModel):
    email: EmailStr
    password: str
    amazon: bool = False
    bestbuy: bool = False

class UserResponse(BaseModel):
    email: EmailStr
    id: int
    createdAt: datetime
    amazon: bool
    bestbuy: bool


    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str

