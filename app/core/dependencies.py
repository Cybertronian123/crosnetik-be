from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Depends, HTTPException
from jose import jwt

from app.core.jwt import SECRET_KEY, ALGORITHM
from app.models.user_model import User

security = HTTPBearer()


async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):

    token = credentials.credentials

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("user_id")

        if user_id is None:
            raise HTTPException(status_code=401)

    except Exception:
        raise HTTPException(status_code=401)

    user = await User.get(user_id)

    if not user:
        raise HTTPException(status_code=401)

    return user