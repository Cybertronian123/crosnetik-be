from fastapi import HTTPException

from app.models.user_model import User
from app.core.security import hash_password, verify_password
from app.core.jwt import create_access_token, create_refresh_token


async def register_user(data):

    existing = await User.find_one(
        {"$or": [{"username": data.username}, {"email": data.email}]}
    )

    if existing:
        raise HTTPException(status_code=400, detail="User already exists")

    user = User(
        firstName=data.firstName,
        lastName=data.lastName,
        username=data.username,
        email=data.email,
        passwordHash=hash_password(data.password),
    )

    await user.insert()

    return user


async def login_user(username: str, password: str):

    user = await User.find_one(User.username == username)

    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    if not verify_password(password, user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    access_token = create_access_token({"user_id": str(user.id)})

    refresh_token = create_refresh_token({"user_id": str(user.id)})

    return {
        "access_token": access_token,
        "refresh_token": refresh_token
    }