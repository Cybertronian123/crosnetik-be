from fastapi import APIRouter
from app.models.user_model import User
from app.core.security import hash_password

router = APIRouter()


# @router.post("/")
# async def create_user(user: UserCreate):

#     user_doc = User(
#         firstName=user.firstName,
#         lastName=user.lastName,
#         username=user.username,
#         email=user.email,
#         passwordHash=hash_password(user.password),
#     )

#     await user_doc.insert()

#     return {"id": str(user_doc.id)}