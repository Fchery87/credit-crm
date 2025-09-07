from enum import Enum
from pydantic import BaseModel, EmailStr

class UserRole(str, Enum):
    OWNER = "owner"
    STAFF = "staff"
    CLIENT = "client"

class UserBase(BaseModel):
    email: EmailStr
    is_active: bool = True
    role: UserRole = UserRole.CLIENT

class UserCreate(UserBase):
    password: str

class UserUpdate(BaseModel):
    email: EmailStr | None = None
    is_active: bool | None = None
    role: UserRole | None = None
    password: str | None = None

class UserInDBBase(UserBase):
    id: int
    account_id: int

    class Config:
        from_attributes = True

class User(UserInDBBase):
    pass

class UserInDB(UserInDBBase):
    hashed_password: str
