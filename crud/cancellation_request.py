from uuid import UUID

from sqlmodel import Session, select

from models.cancellation_request import CancellationRequest
from schemas.cancellation_request import (
    CancellationRequestCreate,
    CancellationRequestUpdate,
)


def create_cancellation_request(
    session: Session,
    cancellation_request_data: CancellationRequestCreate,
):

    cancellation_request = CancellationRequest(
        **cancellation_request_data.model_dump()
    )

    session.add(cancellation_request)
    session.commit()
    session.refresh(cancellation_request)

    return cancellation_request


def get_cancellation_requests(session: Session):

    statement = select(CancellationRequest)

    return session.exec(statement).all()


def get_cancellation_request_by_id(
    session: Session,
    cancellation_request_id: UUID,
):

    return session.get(
        CancellationRequest,
        cancellation_request_id,
    )


def update_cancellation_request(
    session: Session,
    cancellation_request_id: UUID,
    cancellation_request_data: CancellationRequestUpdate,
):

    cancellation_request = session.get(
        CancellationRequest,
        cancellation_request_id,
    )

    if not cancellation_request:
        return None

    updates = cancellation_request_data.model_dump(
        exclude_unset=True
    )

    for key, value in updates.items():
        setattr(cancellation_request, key, value)

    session.add(cancellation_request)
    session.commit()
    session.refresh(cancellation_request)

    return cancellation_request


def delete_cancellation_request(
    session: Session,
    cancellation_request_id: UUID,
):

    cancellation_request = session.get(
        CancellationRequest,
        cancellation_request_id,
    )

    if not cancellation_request:
        return False

    session.delete(cancellation_request)
    session.commit()

    return True