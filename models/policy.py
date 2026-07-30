from uuid import UUID, uuid4
from datetime import datetime

from sqlmodel import SQLModel, Field ,Relationship

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .branch import Branch


class Policy(SQLModel, table=True):

    __tablename__ = "policy"

    id: UUID = Field(default_factory=uuid4, primary_key=True)

    branch_id: UUID = Field(
        foreign_key="branch.id",
        index=True
    )

    title: str

    content: str

    category: str = Field(default="General")

    is_active: bool = Field(default=True)

    created_at: datetime = Field(default_factory=datetime.utcnow)

    updated_at: datetime = Field(default_factory=datetime.utcnow)

    branch: "Branch" = Relationship(
      back_populates="policies"
)