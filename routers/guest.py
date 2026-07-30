from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from database import get_session
from schemas.guest import GuestCreate, GuestRead, GuestUpdate
from crud.guest import (
    create_guest,
    get_guests,
    get_guest_by_id ,
    update_guest ,
    delete_guest
)
from uuid import UUID
router = APIRouter(prefix="/guests", tags=["Guests"])


@router.post("/", response_model=GuestRead)
def create_guest_endpoint(
    guest: GuestCreate,
    session: Session = Depends(get_session)
):
    print(">>> Endpoint reached")
    return create_guest(session, guest)

@router.get("/", response_model=list[GuestRead])
def get_guests_endpoint(
    session: Session = Depends(get_session)
):
    return get_guests(session)

@router.get("/{guest_id}", response_model=GuestRead)
def get_guest_by_id_endpoint(
    guest_id: UUID,
    session: Session = Depends(get_session)
):
    guest = get_guest_by_id(session, guest_id)

    if guest is None:
        raise HTTPException(
            status_code=404,
            detail="Guest not found"
        )

    return guest

@router.put("/{guest_id}", response_model=GuestRead)
def update_guest_endpoint(
    guest_id: UUID,
    guest: GuestUpdate,
    session: Session = Depends(get_session)
):
    updated_guest = update_guest(session, guest_id, guest)

    if updated_guest is None:
        raise HTTPException(
            status_code=404,
            detail="Guest not found"
        )

    return updated_guest

@router.delete("/{guest_id}", response_model=GuestRead)
def delete_guest_endpoint(
    guest_id: UUID,
    session: Session = Depends(get_session)
):
    deleted_guest = delete_guest(session, guest_id)

    if deleted_guest is None:
        raise HTTPException(
            status_code=404,
            detail="Guest not found"
        )

    return deleted_guest