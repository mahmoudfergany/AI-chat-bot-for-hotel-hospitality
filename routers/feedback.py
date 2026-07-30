from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from crud.feedback import (
    create_feedback,
    get_feedbacks,
    get_feedback_by_id,
    update_feedback,
    delete_feedback,
)

from database import get_session

from schemas.feedback import (
    FeedbackCreate,
    FeedbackRead,
    FeedbackUpdate,
)

router = APIRouter(
    prefix="/feedbacks",
    tags=["Feedback"],
)


@router.post("/", response_model=FeedbackRead)
def create_new_feedback(
    feedback_data: FeedbackCreate,
    session: Session = Depends(get_session),
):
    return create_feedback(session, feedback_data)


@router.get("/", response_model=list[FeedbackRead])
def read_feedbacks(
    session: Session = Depends(get_session),
):
    return get_feedbacks(session)


@router.get("/{feedback_id}", response_model=FeedbackRead)
def read_feedback(
    feedback_id: UUID,
    session: Session = Depends(get_session),
):
    feedback = get_feedback_by_id(session, feedback_id)

    if not feedback:
        raise HTTPException(
            status_code=404,
            detail="Feedback not found",
        )

    return feedback


@router.put("/{feedback_id}", response_model=FeedbackRead)
def update_existing_feedback(
    feedback_id: UUID,
    feedback_data: FeedbackUpdate,
    session: Session = Depends(get_session),
):
    feedback = update_feedback(
        session,
        feedback_id,
        feedback_data,
    )

    if not feedback:
        raise HTTPException(
            status_code=404,
            detail="Feedback not found",
        )

    return feedback


@router.delete("/{feedback_id}")
def remove_feedback(
    feedback_id: UUID,
    session: Session = Depends(get_session),
):
    deleted = delete_feedback(session, feedback_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Feedback not found",
        )

    return {
        "message": "Feedback deleted successfully"
    }