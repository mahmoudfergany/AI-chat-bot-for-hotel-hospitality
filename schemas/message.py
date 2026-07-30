from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class MessageCreate(BaseModel):
    conversation_id: UUID
    sender: str
    content: str


class MessageRead(BaseModel):
    id: UUID
    conversation_id: UUID
    sender: str
    content: str
    created_at: datetime


class MessageUpdate(BaseModel):
    sender: str | None = None
    content: str | None = None