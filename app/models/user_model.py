from beanie import Document, Indexed, before_event, Insert, Replace
from pydantic import EmailStr, Field
from datetime import datetime
from typing import Optional


class User(Document):

    first_name: str = Field(..., alias="firstName")
    last_name: str = Field(..., alias="lastName")

    username: Indexed(str, unique=True)
    email: Indexed(EmailStr, unique=True)

    password_hash: str = Field(..., alias="passwordHash")

    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    deleted_at: Optional[datetime] = None

    class Settings:
        name = "users"
        

    class Config:
        populate_by_name = True


    
    @before_event(Insert)
    def set_created(self):
        now = datetime.utcnow()
        self.created_at = now
        self.updated_at = now

    @before_event(Replace)
    def set_updated(self):
        self.updated_at = datetime.utcnow()