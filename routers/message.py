from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from crud.message import (
    create_message,
    get_messages,
    get_message_by_id,
    update_message,
    delete_message,
)
from database import get_session
from schemas.message import (
    MessageCreate,
    MessageRead,
    MessageUpdate,
)

router = APIRouter(
    prefix="/messages",
    tags=["Messages"],
)


@router.post("/", response_model=MessageRead)
def create_new_message(
    message_data: MessageCreate,
    session: Session = Depends(get_session),
):
    return create_message(session, message_data)


@router.get("/", response_model=list[MessageRead])
def read_messages(
    session: Session = Depends(get_session),
):
    return get_messages(session)


@router.get("/{message_id}", response_model=MessageRead)
def read_message(
    message_id: UUID,
    session: Session = Depends(get_session),
):
    message = get_message_by_id(session, message_id)

    if not message:
        raise HTTPException(status_code=404, detail="Message not found")

    return message


@router.put("/{message_id}", response_model=MessageRead)
def update_existing_message(
    message_id: UUID,
    message_data: MessageUpdate,
    session: Session = Depends(get_session),
):
    message = update_message(
        session,
        message_id,
        message_data,
    )

    if not message:
        raise HTTPException(status_code=404, detail="Message not found")

    return message


@router.delete("/{message_id}")
def remove_message(
    message_id: UUID,
    session: Session = Depends(get_session),
):
    deleted = delete_message(session, message_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Message not found")

    return {"message": "Message deleted successfully"}