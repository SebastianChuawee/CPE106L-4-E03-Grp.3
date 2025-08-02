from pydantic import BaseModel, Field
from typing import Optional

class User(BaseModel):
    user_id: str
    name: str
    email: str
    phone: str
    address: str
    is_eld: bool = False  # Elderly person flag
    is_pwd: bool = False  # PWD flag
    registration_date: str

class UserCreate(BaseModel):
    name: str
    email: str
    phone: str
    address: str
    is_eld: bool = False
    is_pwd: bool = False
