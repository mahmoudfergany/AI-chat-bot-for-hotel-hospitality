from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class FAQCreate(BaseModel):
    branch_id: UUID
    question: str
    answer: str
    category: str = "General"


class FAQRead(BaseModel):
    id: UUID
    branch_id: UUID
    question: str
    answer: str
    category: str
    is_active: bool
    created_at: datetime
    updated_at: datetime


class FAQUpdate(BaseModel):
    question: str | None = None
    answer: str | None = None
    category: str | None = None
    is_active: bool | None = None