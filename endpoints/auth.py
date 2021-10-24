from fastapi import APIRouter, Depends, HTTPException, status

from core.security import create_access_token, verify_password
from models.token import Login, Token
from repositories.users import UserRepository

from .depends import get_user_repository

router = APIRouter()


@router.post("/", response_model=Token)
async def login(login: Login, users: UserRepository = Depends(get_user_repository)):
    user = await users.get_by_email(login.email)
    if user is None or not verify_password(login.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Incottect username or password")
    return Token(access_token=create_access_token({"sub": user.email}), token_type="Bearer")
