from uuid import UUID, uuid4
from datetime import datetime

from sqlmodel import SQLModel, Field , Relationship

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .branch import Branch


class KnowledgeDocument(SQLModel, table=True):

    __tablename__ = "knowledge_document"

    id: UUID = Field(default_factory=uuid4, primary_key=True)

    branch_id: UUID = Field(
        foreign_key="branch.id",
        index=True
    )

    title: str

    description: str | None = None

    file_url: str

    document_type: str

    uploaded_by: str

    is_processed: bool = Field(default=False)

    created_at: datetime = Field(default_factory=datetime.utcnow)

    updated_at: datetime = Field(default_factory=datetime.utcnow)

    branch: "Branch" = Relationship(
     back_populates="knowledge_documents"
)