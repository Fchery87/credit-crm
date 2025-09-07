from enum import Enum

class UserRole(str, Enum):
    OWNER = "owner"
    STAFF = "staff"
    CLIENT = "client"
