from pydantic import BaseModel

class Message(BaseModel):
    message: str
    password_reset_token: str | None = None
