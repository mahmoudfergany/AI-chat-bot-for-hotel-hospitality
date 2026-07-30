from uuid import UUID

from sqlmodel import SQLModel


class GuestCreate(SQLModel):
    first_name: str
    last_name: str
    email: str
    phone: str


class GuestRead(SQLModel):
    id: UUID
    first_name: str
    last_name: str
    email: str
    phone: str

class GuestUpdate(SQLModel):
    first_name: str
    last_name: str
    email: str
    phone: str