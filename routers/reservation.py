from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from crud.reservation import (
    create_reservation,
    get_reservations,
    get_reservation_by_id,
    update_reservation,
    delete_reservation,
)

from database import get_session

from schemas.reservation import (
    ReservationCreate,
    ReservationRead,
    ReservationUpdate,
)

router = APIRouter(
    prefix="/reservations",
    tags=["Reservations"],
)


@router.post("/", response_model=ReservationRead)
def create_new_reservation(
    reservation_data: ReservationCreate,
    session: Session = Depends(get_session),
):
    return create_reservation(
        session,
        reservation_data,
    )


@router.get("/", response_model=list[ReservationRead])
def read_reservations(
    session: Session = Depends(get_session),
):
    return get_reservations(session)


@router.get("/{reservation_id}", response_model=ReservationRead)
def read_reservation(
    reservation_id: UUID,
    session: Session = Depends(get_session),
):
    reservation = get_reservation_by_id(
        session,
        reservation_id,
    )

    if not reservation:
        raise HTTPException(
            status_code=404,
            detail="Reservation not found",
        )

    return reservation


@router.put("/{reservation_id}", response_model=ReservationRead)
def update_existing_reservation(
    reservation_id: UUID,
    reservation_data: ReservationUpdate,
    session: Session = Depends(get_session),
):
    reservation = update_reservation(
        session,
        reservation_id,
        reservation_data,
    )

    if not reservation:
        raise HTTPException(
            status_code=404,
            detail="Reservation not found",
        )

    return reservation


@router.delete("/{reservation_id}")
def remove_reservation(
    reservation_id: UUID,
    session: Session = Depends(get_session),
):
    deleted = delete_reservation(
        session,
        reservation_id,
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Reservation not found",
        )

    return {
        "message": "Reservation deleted successfully"
    }