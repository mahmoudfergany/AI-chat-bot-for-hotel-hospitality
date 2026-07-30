from uuid import UUID

from sqlmodel import Session, select

from models.faq import FAQ
from schemas.faq import (
    FAQCreate,
    FAQUpdate,
)


def create_faq(session: Session, faq_data: FAQCreate):

    faq = FAQ(**faq_data.model_dump())

    session.add(faq)
    session.commit()
    session.refresh(faq)

    return faq


def get_faqs(session: Session):

    statement = select(FAQ)

    return session.exec(statement).all()


def get_faq_by_id(session: Session, faq_id: UUID):

    return session.get(FAQ, faq_id)


def update_faq(
    session: Session,
    faq_id: UUID,
    faq_data: FAQUpdate,
):

    faq = session.get(FAQ, faq_id)

    if not faq:
        return None

    updates = faq_data.model_dump(exclude_unset=True)

    for key, value in updates.items():
        setattr(faq, key, value)

    session.add(faq)
    session.commit()
    session.refresh(faq)

    return faq


def delete_faq(session: Session, faq_id: UUID):

    faq = session.get(FAQ, faq_id)

    if not faq:
        return False

    session.delete(faq)
    session.commit()

    return True