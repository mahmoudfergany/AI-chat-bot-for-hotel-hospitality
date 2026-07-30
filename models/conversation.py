from uuid import UUID, uuid4
from datetime import datetime

from sqlmodel import SQLModel, Field, Relationship
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .branch import Branch
    from .guest import Guest

if TYPE_CHECKING:
    from .message import Message

if TYPE_CHECKING:
    from .feedback import Feedback

class Conversation(SQLModel, table=True):

    __tablename__ = "conversation"

    id: UUID = Field(default_factory=uuid4, primary_key=True)

    guest_id: UUID = Field(
        foreign_key="guest.id",
        index=True
    )

    branch_id: UUID = Field(
        foreign_key="branch.id",
        index=True
    )

    started_at: datetime = Field(default_factory=datetime.utcnow)

    ended_at: datetime | None = None

    status: str = Field(default="active")


    guest: "Guest" = Relationship(
     back_populates="conversations"
     )


    messages: list["Message"] = Relationship(
     back_populates="conversation"
    )


    feedbacks: list["Feedback"] = Relationship(
     back_populates="conversation"
    )
    branch: "Branch" = Relationship(
     back_populates="conversations"
    )