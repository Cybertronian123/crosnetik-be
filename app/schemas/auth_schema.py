from pydantic import BaseModel, EmailStr


class RegisterRequest(BaseModel):
    firstName: str
    lastName: str
    username: str
    email: EmailStr
    password: str


class LoginRequest(BaseModel):
    username: str
    password: str


class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"

