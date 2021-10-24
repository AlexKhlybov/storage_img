import datetime
from typing import Optional

from pydantic import BaseModel


class Inbox(BaseModel):
    id: Optional[int] = None
    name: str
    code: str
    created_at: datetime.datetime


class InboxIn(BaseModel):
    name: str
    code: str
