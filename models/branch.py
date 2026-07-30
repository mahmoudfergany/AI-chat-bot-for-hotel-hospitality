from uuid import UUID, uuid4
from datetime import datetime

from sqlmodel import SQLModel, Field, Relationship
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .conversation import Conversation
    from .support_ticket import SupportTicket
    from .chain import Chain
    from .reservation import Reservation
    from .faq import FAQ
    from .policy import Policy
    from .knowledge_document import KnowledgeDocument


class Branch(SQLModel, table=True):

    __tablename__ = "branch"

    id: UUID = Field(default_factory=uuid4, primary_key=True)

    chain_id: UUID = Field(
        foreign_key="chain.id",
        index=True
    )

    name: str
    address: str
    city: str
    country: str

    description: str | None = None

    is_active: bool = Field(default=True)

    created_at: datetime = Field(default_factory=datetime.utcnow)

    reservations: list["Reservation"] = Relationship(
        back_populates="branch"
    )

    faqs: list["FAQ"] = Relationship(
        back_populates="branch"
    )

    policies: list["Policy"] = Relationship(
        back_populates="branch"
    )

    knowledge_documents: list["KnowledgeDocument"] = Relationship(
        back_populates="branch"
    )

    conversations: list["Conversation"] = Relationship(
        back_populates="branch"
    )
    support_tickets: list["SupportTicket"] = Relationship(
        back_populates="branch"
    )
    chain: "Chain" = Relationship(
        back_populates="branches"
    )