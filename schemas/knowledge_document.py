from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class KnowledgeDocumentCreate(BaseModel):
    branch_id: UUID
    title: str
    description: str | None = None
    file_url: str
    document_type: str
    uploaded_by: str


class KnowledgeDocumentRead(BaseModel):
    id: UUID
    branch_id: UUID
    title: str
    description: str | None = None
    file_url: str
    document_type: str
    uploaded_by: str
    is_processed: bool
    created_at: datetime
    updated_at: datetime


class KnowledgeDocumentUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    file_url: str | None = None
    document_type: str | None = None
    uploaded_by: str | None = None
    is_processed: bool | None = None