from uuid import UUID
from datetime import datetime

from sqlmodel import SQLModel


class ChainCreate(SQLModel):
    name: str
    description: str | None = None


class ChainRead(SQLModel):
    id: UUID
    name: str
    description: str | None = None
    is_active: bool
    created_at: datetime


class ChainUpdate(SQLModel):
    name: str
    description: str | None = None
    is_active: bool