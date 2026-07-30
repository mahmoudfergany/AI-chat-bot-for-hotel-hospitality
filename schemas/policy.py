from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class PolicyCreate(BaseModel):
    branch_id: UUID
    title: str
    content: str
    category: str = "General"


class PolicyRead(BaseModel):
    id: UUID
    branch_id: UUID
    title: str
    content: str
    category: str
    is_active: bool
    created_at: datetime
    updated_at: datetime


class PolicyUpdate(BaseModel):
    title: str | None = None
    content: str | None = None
    category: str | None = None
    is_active: bool | None = None