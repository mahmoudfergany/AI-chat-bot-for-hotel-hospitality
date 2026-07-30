from uuid import UUID, uuid4
from datetime import datetime

from sqlmodel import SQLModel, Field, Relationship
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .guest import Guest

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .branch import Branch

if TYPE_CHECKING:
    from .cancellation_request import CancellationRequest

class Reservation(SQLModel, table=True):

    __tablename__ = "reservation"

    id: UUID = Field(default_factory=uuid4, primary_key=True)

    guest_id: UUID = Field(
        foreign_key="guest.id",
        index=True
    )

    branch_id: UUID = Field(
        foreign_key="branch.id",
        index=True
    )

    check_in: datetime
    check_out: datetime

    number_of_guests: int

    status: str = Field(default="Pending")
    created_at: datetime = Field(default_factory=datetime.utcnow)

    guest: "Guest" = Relationship(
        back_populates="reservations"
    )

    branch: "Branch" = Relationship(
        back_populates="reservations"
    )

    cancellation_requests: list["CancellationRequest"] = Relationship(
        back_populates="reservation"
    )