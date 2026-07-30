from sqlmodel import Session, select

from models.guest import Guest
from schemas.guest import GuestCreate, GuestUpdate
from uuid import UUID


def create_guest(session: Session, guest_data: GuestCreate):
    guest = Guest(
        first_name=guest_data.first_name,
        last_name=guest_data.last_name,
        email=guest_data.email,
        phone=guest_data.phone,
    )

    session.add(guest)
    session.commit()
    session.refresh(guest)

    return guest


def get_guests(session: Session):
    statement = select(Guest)
    guests = session.exec(statement).all()
    return guests

def get_guest_by_id(session: Session, guest_id: UUID):
    guest = session.get(Guest, guest_id)
    return guest

def update_guest(
    session: Session,
    guest_id: UUID,
    guest_data: GuestUpdate
):
    guest = session.get(Guest, guest_id)

    if guest is None:
        return None

    guest.first_name = guest_data.first_name
    guest.last_name = guest_data.last_name
    guest.email = guest_data.email
    guest.phone = guest_data.phone

    session.commit()
    session.refresh(guest)

    return guest

def delete_guest(
    session: Session,
    guest_id: UUID
):
    guest = session.get(Guest, guest_id)

    if guest is None:
        return None

    session.delete(guest)
    session.commit()

    return guest