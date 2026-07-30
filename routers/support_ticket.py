from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from crud.support_ticket import (
    create_support_ticket,
    get_support_tickets,
    get_support_ticket_by_id,
    update_support_ticket,
    delete_support_ticket,
)

from database import get_session

from schemas.support_ticket import (
    SupportTicketCreate,
    SupportTicketRead,
    SupportTicketUpdate,
)

router = APIRouter(
    prefix="/support-tickets",
    tags=["Support Tickets"],
)


@router.post("/", response_model=SupportTicketRead)
def create_new_support_ticket(
    support_ticket_data: SupportTicketCreate,
    session: Session = Depends(get_session),
):
    return create_support_ticket(
        session,
        support_ticket_data,
    )


@router.get("/", response_model=list[SupportTicketRead])
def read_support_tickets(
    session: Session = Depends(get_session),
):
    return get_support_tickets(session)


@router.get("/{support_ticket_id}", response_model=SupportTicketRead)
def read_support_ticket(
    support_ticket_id: UUID,
    session: Session = Depends(get_session),
):
    support_ticket = get_support_ticket_by_id(
        session,
        support_ticket_id,
    )

    if not support_ticket:
        raise HTTPException(
            status_code=404,
            detail="Support ticket not found",
        )

    return support_ticket


@router.put("/{support_ticket_id}", response_model=SupportTicketRead)
def update_existing_support_ticket(
    support_ticket_id: UUID,
    support_ticket_data: SupportTicketUpdate,
    session: Session = Depends(get_session),
):
    support_ticket = update_support_ticket(
        session,
        support_ticket_id,
        support_ticket_data,
    )

    if not support_ticket:
        raise HTTPException(
            status_code=404,
            detail="Support ticket not found",
        )

    return support_ticket


@router.delete("/{support_ticket_id}")
def remove_support_ticket(
    support_ticket_id: UUID,
    session: Session = Depends(get_session),
):
    deleted = delete_support_ticket(
        session,
        support_ticket_id,
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Support ticket not found",
        )

    return {
        "message": "Support ticket deleted successfully"
    }