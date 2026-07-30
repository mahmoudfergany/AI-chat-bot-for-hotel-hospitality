from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class ConversationCreate(BaseModel):
    guest_id: UUID
    branch_id: UUID


class ConversationRead(BaseModel):
    id: UUID
    guest_id: UUID
    branch_id: UUID
    started_at: datetime
    ended_at: datetime | None = None
    status: str


class ConversationUpdate(BaseModel):
    ended_at: datetime | None = None
    status: str | None = None