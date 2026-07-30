from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from crud.cancellation_request import (
    create_cancellation_request,
    get_cancellation_requests,
    get_cancellation_request_by_id,
    update_cancellation_request,
    delete_cancellation_request,
)

from database import get_session

from schemas.cancellation_request import (
    CancellationRequestCreate,
    CancellationRequestRead,
    CancellationRequestUpdate,
)

router = APIRouter(
    prefix="/cancellation-requests",
    tags=["Cancellation Requests"],
)


@router.post("/", response_model=CancellationRequestRead)
def create_new_cancellation_request(
    cancellation_request_data: CancellationRequestCreate,
    session: Session = Depends(get_session),
):
    return create_cancellation_request(
        session,
        cancellation_request_data,
    )


@router.get("/", response_model=list[CancellationRequestRead])
def read_cancellation_requests(
    session: Session = Depends(get_session),
):
    return get_cancellation_requests(session)


@router.get("/{cancellation_request_id}", response_model=CancellationRequestRead)
def read_cancellation_request(
    cancellation_request_id: UUID,
    session: Session = Depends(get_session),
):
    cancellation_request = get_cancellation_request_by_id(
        session,
        cancellation_request_id,
    )

    if not cancellation_request:
        raise HTTPException(
            status_code=404,
            detail="Cancellation request not found",
        )

    return cancellation_request


@router.put("/{cancellation_request_id}", response_model=CancellationRequestRead)
def update_existing_cancellation_request(
    cancellation_request_id: UUID,
    cancellation_request_data: CancellationRequestUpdate,
    session: Session = Depends(get_session),
):
    cancellation_request = update_cancellation_request(
        session,
        cancellation_request_id,
        cancellation_request_data,
    )

    if not cancellation_request:
        raise HTTPException(
            status_code=404,
            detail="Cancellation request not found",
        )

    return cancellation_request


@router.delete("/{cancellation_request_id}")
def remove_cancellation_request(
    cancellation_request_id: UUID,
    session: Session = Depends(get_session),
):
    deleted = delete_cancellation_request(
        session,
        cancellation_request_id,
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Cancellation request not found",
        )

    return {
        "message": "Cancellation request deleted successfully"
    }