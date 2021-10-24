from typing import List

from fastapi import APIRouter, Depends, HTTPException, status

from models.inbox import Inbox, InboxIn
from repositories.inbox import InboxRepository
from repositories.users import UserRepository

from .depends import get_frame_repository

router = APIRouter()


@router.get("/", response_model=List[Inbox])
async def read_frames(frames: InboxRepository = Depends(get_frame_repository), limit: int = 100, skip: int = 100):
    return await frames.get_all(limit=limit, skip=0)


@router.post("/", response_model=Inbox)
async def create_frame(frame: InboxIn, frames: InboxRepository = Depends(get_frame_repository)):
    return await frames.created(u=frame)


@router.delete("/{frame_id}")
async def delete_frame(id: int, frames: InboxRepository = Depends(get_frame_repository)):
    frame = await frames.get_by_id(id=id)
    if frame is None:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found frame")
    return await frames.deleted(id=id)
