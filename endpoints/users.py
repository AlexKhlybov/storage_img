from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.sql.schema import PrimaryKeyConstraint

from models.user import User, UserIn
from repositories.users import UserRepository

from .depends import get_current_user, get_user_repository

router = APIRouter()


@router.get("/", response_model=List[User], response_model_exclude={"hashed_password"})
async def read_users(users: UserRepository = Depends(get_user_repository), limit: int = 100, skip: int = 100):
    return await users.get_all(limit=limit, skip=0)


@router.post("/", response_model=User, response_model_exclude={"hashed_password"})
async def create_user(user: UserIn, users: UserRepository = Depends(get_user_repository)):
    return await users.created(u=user)


@router.put("/{user_id}", response_model=User, response_model_exclude={"hashed_password"})
async def update_user(
    id: int,
    user: UserIn,
    users: UserRepository = Depends(get_user_repository),
    current_user: User = Depends(get_current_user),
):
    old_user = await users.get_by_id(id=id)
    if old_user is None or old_user.email != current_user.email:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found user")
    return await users.update(id=id, u=user)
