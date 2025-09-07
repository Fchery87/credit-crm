from enum import Enum
from pydantic import BaseModel, EmailStr

class UserRole(str, Enum):
    OWNER = "owner"
    STAFF = "staff"
    CLIENT = "client"

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    role: UserRole
