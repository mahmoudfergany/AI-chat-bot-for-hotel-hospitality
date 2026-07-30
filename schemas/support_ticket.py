from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class SupportTicketCreate(BaseModel):
    guest_id: UUID
    branch_id: UUID
    title: str
    description: str


class SupportTicketRead(BaseModel):
    id: UUID
    guest_id: UUID
    branch_id: UUID
    title: str
    description: str
    status: str
    created_at: datetime


class SupportTicketUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    status: str | None = None