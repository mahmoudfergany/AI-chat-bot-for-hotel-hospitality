from datetime import date
from uuid import UUID

from pydantic import BaseModel


class ReservationCreate(BaseModel):
    guest_id: UUID
    branch_id: UUID
    check_in: date
    check_out: date
    number_of_guests: int


class ReservationRead(BaseModel):
    id: UUID
    guest_id: UUID
    branch_id: UUID
    check_in: date
    check_out: date
    number_of_guests: int
    status: str


class ReservationUpdate(BaseModel):
    guest_id: UUID | None = None
    branch_id: UUID | None = None
    check_in: date | None = None
    check_out: date | None = None
    number_of_guests: int | None = None
    status: str | None = None