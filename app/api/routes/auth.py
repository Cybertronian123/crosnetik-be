from fastapi import APIRouter, HTTPException
from fastapi import Depends

from app.schemas.auth_schema import RegisterRequest, LoginRequest, TokenResponse
from app.services.auth_service import register_user, login_user
from app.core.dependencies import get_current_user

router = APIRouter()


@router.post("/register")
async def register(data: RegisterRequest):

    try:
        user = await register_user(data)
        return {"id": str(user.id)}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.post("/login", response_model=TokenResponse)
async def login(data: LoginRequest):

    tokens = await login_user(data.username, data.password)

    return tokens


@router.get("/me")
async def get_me(user=Depends(get_current_user)):
    return {
        "id": str(user.id),
        "username": user.username,
        "email": user.email
    }

