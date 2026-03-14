from pydantic import BaseModel, EmailStr
from datetime import datetime



class UserResponse(BaseModel):
    id: str
    firstName: str
    lastName: str
    username: str
    email: EmailStr
    created_at: datetime