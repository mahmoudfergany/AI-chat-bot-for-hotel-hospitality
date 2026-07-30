from uuid import UUID

from sqlmodel import Session, select

from models.message import Message
from schemas.message import (
    MessageCreate,
    MessageUpdate,
)


def create_message(session: Session, message_data: MessageCreate):

    message = Message(**message_data.model_dump())

    session.add(message)
    session.commit()
    session.refresh(message)

    return message


def get_messages(session: Session):

    statement = select(Message)

    return session.exec(statement).all()


def get_message_by_id(session: Session, message_id: UUID):

    return session.get(Message, message_id)


def update_message(
    session: Session,
    message_id: UUID,
    message_data: MessageUpdate,
):

    message = session.get(Message, message_id)

    if not message:
        return None

    updates = message_data.model_dump(exclude_unset=True)

    for key, value in updates.items():
        setattr(message, key, value)

    session.add(message)
    session.commit()
    session.refresh(message)

    return message


def delete_message(session: Session, message_id: UUID):

    message = session.get(Message, message_id)

    if not message:
        return False

    session.delete(message)
    session.commit()

    return True