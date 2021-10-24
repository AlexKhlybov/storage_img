from datetime import datetime
from typing import List, Optional

from core.security import hash_password
from db.inbox import inbox
from db.users import users
from models.inbox import Inbox, InboxIn

from .base import BaseRepository


class InboxRepository(BaseRepository):
    async def get_all(self, limit: int = 100, skip: int = 0) -> List[Inbox]:
        query = inbox.select().limit(limit).offset(skip)
        return await self.database.fetch_all(query=query)

    async def get_by_id(self, id: int) -> Optional[Inbox]:
        query = inbox.select().where(inbox.c.id == id)
        user = await self.database.fetch_one(query)
        if user is None:
            return None
        return Inbox.parse_obj(user)

    async def created(self, data: dict) -> Inbox:
        frame = Inbox(name=data["filename"], code=data["code"], created_at=datetime.now())

        values = {**frame.dict()}
        values.pop("id", None)
        query = inbox.insert().values(**values)
        frame.id = await self.database.execute(query)
        return frame

    async def deleted(self, id: int):
        query = inbox.delete().where(inbox.c.id == id)
        return await self.database.execute(query)
