from uuid import UUID

from sqlmodel import Session, select

from models.feedback import Feedback
from schemas.feedback import (
    FeedbackCreate,
    FeedbackUpdate,
)


def create_feedback(
    session: Session,
    feedback_data: FeedbackCreate,
):

    feedback = Feedback(**feedback_data.model_dump())

    session.add(feedback)
    session.commit()
    session.refresh(feedback)

    return feedback


def get_feedbacks(session: Session):

    statement = select(Feedback)

    return session.exec(statement).all()


def get_feedback_by_id(
    session: Session,
    feedback_id: UUID,
):

    return session.get(Feedback, feedback_id)


def update_feedback(
    session: Session,
    feedback_id: UUID,
    feedback_data: FeedbackUpdate,
):

    feedback = session.get(
        Feedback,
        feedback_id,
    )

    if not feedback:
        return None

    updates = feedback_data.model_dump(
        exclude_unset=True
    )

    for key, value in updates.items():
        setattr(feedback, key, value)

    session.add(feedback)
    session.commit()
    session.refresh(feedback)

    return feedback


def delete_feedback(
    session: Session,
    feedback_id: UUID,
):

    feedback = session.get(
        Feedback,
        feedback_id,
    )

    if not feedback:
        return False

    session.delete(feedback)
    session.commit()

    return True