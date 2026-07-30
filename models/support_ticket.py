from uuid import UUID, uuid4
from datetime import datetime

from sqlmodel import SQLModel, Field ,Relationship


from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .branch import Branch
    from .guest import Guest


class SupportTicket(SQLModel, table=True):

    __tablename__ = "support_ticket"

    id: UUID = Field(default_factory=uuid4, primary_key=True)

    guest_id: UUID = Field(
        foreign_key="guest.id",
        index=True
    )

    branch_id: UUID = Field(
        foreign_key="branch.id",
        index=True
    )

    title: str

    description: str

    status: str = Field(default="open")

    created_at: datetime = Field(default_factory=datetime.utcnow)


    guest: "Guest" = Relationship(
      back_populates="support_tickets"
    )
    branch: "Branch" = Relationship(
      back_populates="support_tickets"
    )