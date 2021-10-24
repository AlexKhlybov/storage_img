import datetime

from pydantic import BaseModel


class Inbox(BaseModel):
    id: int
    name: str
    code: str
    created_at: datetime.datetime


class InboxIn(BaseModel):
    name: str
    code: str
