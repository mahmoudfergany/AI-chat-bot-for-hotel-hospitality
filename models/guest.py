from uuid import UUID, uuid4
from datetime import datetime
from typing import TYPE_CHECKING

from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from .reservation import Reservation
    from .conversation import Conversation
    from .feedback import Feedback
    from .support_ticket import SupportTicket


class Guest(SQLModel, table=True):
    __tablename__ = "guest"

    id: UUID = Field(default_factory=uuid4, primary_key=True)

    first_name: str
    last_name: str

    email: str = Field(unique=True, index=True)

    phone: str

    preferred_language: str = Field(default="en")

    is_active: bool = Field(default=True)

    created_at: datetime = Field(default_factory=datetime.utcnow)

    updated_at: datetime = Field(default_factory=datetime.utcnow)

    reservations: list["Reservation"] = Relationship(
        back_populates="guest"
    )

    conversations: list["Conversation"] = Relationship(
        back_populates="guest"
    )

    feedbacks: list["Feedback"] = Relationship(
        back_populates="guest"
    )

    support_tickets: list["SupportTicket"] = Relationship(
        back_populates="guest"
    )