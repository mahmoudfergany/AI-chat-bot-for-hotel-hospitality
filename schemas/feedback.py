from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class FeedbackCreate(BaseModel):
    guest_id: UUID
    conversation_id: UUID
    rating: int
    comment: str | None = None


class FeedbackRead(BaseModel):
    id: UUID
    guest_id: UUID
    conversation_id: UUID
    rating: int
    comment: str | None = None
    created_at: datetime


class FeedbackUpdate(BaseModel):
    rating: int | None = None
    comment: str | None = None