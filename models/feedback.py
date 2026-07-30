from uuid import UUID, uuid4
from datetime import datetime

from sqlmodel import SQLModel, Field, Relationship
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .conversation import Conversation

if TYPE_CHECKING:
    from .guest import Guest

class Feedback(SQLModel, table=True):

    __tablename__ = "feedback"

    id: UUID = Field(default_factory=uuid4, primary_key=True)

    guest_id: UUID = Field(
        foreign_key="guest.id",
        index=True
    )

    conversation_id: UUID = Field(
        foreign_key="conversation.id",
        index=True
    )

    rating: int

    comment: str | None = None

    created_at: datetime = Field(default_factory=datetime.utcnow)


    conversation: "Conversation" = Relationship(
    back_populates="feedbacks"
      )

    guest: "Guest" = Relationship(
    back_populates="feedbacks"
     )