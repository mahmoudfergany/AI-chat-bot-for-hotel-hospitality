from sqlmodel import SQLModel, Field, Relationship
from typing import TYPE_CHECKING
from uuid import UUID, uuid4
from datetime import datetime

if TYPE_CHECKING:
    from .branch import Branch


class Chain(SQLModel, table=True):

    __tablename__ = "chain"

    id: UUID = Field(default_factory=uuid4, primary_key=True)

    name: str = Field(index=True, unique=True)

    description: str | None = None

    is_active: bool = Field(default=True)

    created_at: datetime = Field(default_factory=datetime.utcnow)

    branches: list["Branch"] = Relationship(
        back_populates="chain"
    )