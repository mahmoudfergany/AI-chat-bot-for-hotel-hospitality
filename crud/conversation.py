from uuid import UUID

from sqlmodel import Session, select

from models.conversation import Conversation
from schemas.conversation import (
    ConversationCreate,
    ConversationUpdate,
)


def create_conversation(session: Session, conversation_data: ConversationCreate):

    conversation = Conversation(**conversation_data.model_dump())

    session.add(conversation)
    session.commit()
    session.refresh(conversation)

    return conversation


def get_conversations(session: Session):

    statement = select(Conversation)

    return session.exec(statement).all()


def get_conversation_by_id(session: Session, conversation_id: UUID):

    return session.get(Conversation, conversation_id)


def update_conversation(
    session: Session,
    conversation_id: UUID,
    conversation_data: ConversationUpdate,
):

    conversation = session.get(Conversation, conversation_id)

    if not conversation:
        return None

    updates = conversation_data.model_dump(exclude_unset=True)

    for key, value in updates.items():
        setattr(conversation, key, value)

    session.add(conversation)
    session.commit()
    session.refresh(conversation)

    return conversation


def delete_conversation(session: Session, conversation_id: UUID):

    conversation = session.get(Conversation, conversation_id)

    if not conversation:
        return False

    session.delete(conversation)
    session.commit()

    return True