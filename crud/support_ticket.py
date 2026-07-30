from uuid import UUID

from sqlmodel import Session, select

from models.support_ticket import SupportTicket
from schemas.support_ticket import (
    SupportTicketCreate,
    SupportTicketUpdate,
)


def create_support_ticket(
    session: Session,
    support_ticket_data: SupportTicketCreate,
):

    support_ticket = SupportTicket(
        **support_ticket_data.model_dump()
    )

    session.add(support_ticket)
    session.commit()
    session.refresh(support_ticket)

    return support_ticket


def get_support_tickets(session: Session):

    statement = select(SupportTicket)

    return session.exec(statement).all()


def get_support_ticket_by_id(
    session: Session,
    support_ticket_id: UUID,
):

    return session.get(
        SupportTicket,
        support_ticket_id,
    )


def update_support_ticket(
    session: Session,
    support_ticket_id: UUID,
    support_ticket_data: SupportTicketUpdate,
):

    support_ticket = session.get(
        SupportTicket,
        support_ticket_id,
    )

    if not support_ticket:
        return None

    updates = support_ticket_data.model_dump(
        exclude_unset=True
    )

    for key, value in updates.items():
        setattr(support_ticket, key, value)

    session.add(support_ticket)
    session.commit()
    session.refresh(support_ticket)

    return support_ticket


def delete_support_ticket(
    session: Session,
    support_ticket_id: UUID,
):

    support_ticket = session.get(
        SupportTicket,
        support_ticket_id,
    )

    if not support_ticket:
        return False

    session.delete(support_ticket)
    session.commit()

    return True