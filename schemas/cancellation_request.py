from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class CancellationRequestCreate(BaseModel):
    reservation_id: UUID
    reason: str


class CancellationRequestRead(BaseModel):
    id: UUID
    reservation_id: UUID
    reason: str
    status: str
    requested_at: datetime


class CancellationRequestUpdate(BaseModel):
    reason: str | None = None
    status: str | None = None