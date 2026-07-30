from uuid import UUID, uuid4
from datetime import datetime

from sqlmodel import SQLModel, Field, Relationship
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .reservation import Reservation

class CancellationRequest(SQLModel, table=True):

    __tablename__ = "cancellation_request"

    id: UUID = Field(default_factory=uuid4, primary_key=True)

    reservation_id: UUID = Field(
        foreign_key="reservation.id",
        index=True
    )

    reason: str

    status: str = Field(default="pending")

    requested_at: datetime = Field(default_factory=datetime.utcnow)

    reservation: "Reservation" = Relationship(
    back_populates="cancellation_requests"
)