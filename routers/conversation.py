from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from crud.conversation import (
    create_conversation,
    get_conversations,
    get_conversation_by_id,
    update_conversation,
    delete_conversation,
)
from database import get_session
from schemas.conversation import (
    ConversationCreate,
    ConversationRead,
    ConversationUpdate,
)

router = APIRouter(
    prefix="/conversations",
    tags=["Conversations"],
)


@router.post("/", response_model=ConversationRead)
def create_new_conversation(
    conversation_data: ConversationCreate,
    session: Session = Depends(get_session),
):
    return create_conversation(session, conversation_data)


@router.get("/", response_model=list[ConversationRead])
def read_conversations(
    session: Session = Depends(get_session),
):
    return get_conversations(session)


@router.get("/{conversation_id}", response_model=ConversationRead)
def read_conversation(
    conversation_id: UUID,
    session: Session = Depends(get_session),
):
    conversation = get_conversation_by_id(session, conversation_id)

    if not conversation:
        raise HTTPException(status_code=404, detail="Conversation not found")

    return conversation


@router.put("/{conversation_id}", response_model=ConversationRead)
def update_existing_conversation(
    conversation_id: UUID,
    conversation_data: ConversationUpdate,
    session: Session = Depends(get_session),
):
    conversation = update_conversation(
        session,
        conversation_id,
        conversation_data,
    )

    if not conversation:
        raise HTTPException(status_code=404, detail="Conversation not found")

    return conversation


@router.delete("/{conversation_id}")
def remove_conversation(
    conversation_id: UUID,
    session: Session = Depends(get_session),
):
    deleted = delete_conversation(session, conversation_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Conversation not found")

    return {"message": "Conversation deleted successfully"}