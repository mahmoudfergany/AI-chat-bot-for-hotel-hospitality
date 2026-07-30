from uuid import UUID, uuid4
from datetime import datetime

from sqlmodel import SQLModel, Field, Relationship
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .conversation import Conversation

class Message(SQLModel, table=True):

    __tablename__ = "message"

    id: UUID = Field(default_factory=uuid4, primary_key=True)

    conversation_id: UUID = Field(
        foreign_key="conversation.id",
        index=True
    )

    sender: str

    content: str

    created_at: datetime = Field(default_factory=datetime.utcnow)

    conversation: "Conversation" = Relationship(
      back_populates="messages"
)