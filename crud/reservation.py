from uuid import UUID

from sqlmodel import Session, select

from models.reservation import Reservation
from schemas.reservation import ReservationCreate, ReservationUpdate


def create_reservation(
    session: Session,
    reservation_data: ReservationCreate,
):
    print("reservation_data =", reservation_data)
    print("model_dump =", reservation_data.model_dump())

    reservation = Reservation(
        guest_id=reservation_data.guest_id,
        branch_id=reservation_data.branch_id,
        check_in=reservation_data.check_in,
        check_out=reservation_data.check_out,
        number_of_guests=reservation_data.number_of_guests,
        status="Pending",
    )
    
    session.add(reservation)
    session.commit()
    session.refresh(reservation)

    return reservation


def get_reservations(session: Session):

    statement = select(Reservation)

    return session.exec(statement).all()


def get_reservation_by_id(
    session: Session,
    reservation_id: UUID,
):

    return session.get(Reservation, reservation_id)


def update_reservation(
    session: Session,
    reservation_id: UUID,
    reservation_data: ReservationUpdate,
):

    reservation = session.get(
        Reservation,
        reservation_id,
    )

    if not reservation:
        return None

    updates = reservation_data.model_dump(
        exclude_unset=True
    )

    for key, value in updates.items():
        setattr(reservation, key, value)

    session.add(reservation)
    session.commit()
    session.refresh(reservation)

    return reservation


def delete_reservation(
    session: Session,
    reservation_id: UUID,
):

    reservation = session.get(
        Reservation,
        reservation_id,
    )

    if not reservation:
        return False

    session.delete(reservation)
    session.commit()

    return True