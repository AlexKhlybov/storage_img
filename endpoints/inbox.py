import os
import uuid
from datetime import datetime
from typing import List

from fastapi import (APIRouter, Depends, File, HTTPException, Request,
                     UploadFile, status)

from models.inbox import Inbox, InboxIn
from repositories.inbox import InboxRepository
from repositories.users import UserRepository

from .depends import get_frame_repository
from .file import create_file, delete_file

router = APIRouter()


@router.get("/", response_model=List[Inbox])
async def read_frames(frames: InboxRepository = Depends(get_frame_repository), limit: int = 100, skip: int = 100):
    return await frames.get_all(limit=limit, skip=0)


@router.post("/", response_model=List[Inbox])
async def create_frame(
    request: Request, frames: InboxRepository = Depends(get_frame_repository), up_file: List[UploadFile] = File(...)
):
    if len(up_file) > 15:
        raise HTTPException(status_code=400, detail="I can't do more than 15 at a time!")
    frame_list = []
    for file in up_file:
        frame = {"code": request.url.path, "filename": await create_file(file)}
        frame_list.append(await frames.created(data=frame))
    return frame_list


@router.delete("/{id}")
async def delete_frame(id: int, frames: InboxRepository = Depends(get_frame_repository)):
    frame = await frames.get_by_id(id=id)
    from icecream import ic

    if frame is None:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found frame")
    delete_file(frame)
    return {"status": True}
