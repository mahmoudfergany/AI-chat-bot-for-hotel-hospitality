from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from crud.faq import (
    create_faq,
    get_faqs,
    get_faq_by_id,
    update_faq,
    delete_faq,
)
from database import get_session
from schemas.faq import (
    FAQCreate,
    FAQRead,
    FAQUpdate,
)

router = APIRouter(
    prefix="/faqs",
    tags=["FAQs"],
)


@router.post("/", response_model=FAQRead)
def create_new_faq(
    faq_data: FAQCreate,
    session: Session = Depends(get_session),
):
    return create_faq(session, faq_data)


@router.get("/", response_model=list[FAQRead])
def read_faqs(
    session: Session = Depends(get_session),
):
    return get_faqs(session)


@router.get("/{faq_id}", response_model=FAQRead)
def read_faq(
    faq_id: UUID,
    session: Session = Depends(get_session),
):
    faq = get_faq_by_id(session, faq_id)

    if not faq:
        raise HTTPException(status_code=404, detail="FAQ not found")

    return faq


@router.put("/{faq_id}", response_model=FAQRead)
def update_existing_faq(
    faq_id: UUID,
    faq_data: FAQUpdate,
    session: Session = Depends(get_session),
):
    faq = update_faq(
        session,
        faq_id,
        faq_data,
    )

    if not faq:
        raise HTTPException(status_code=404, detail="FAQ not found")

    return faq


@router.delete("/{faq_id}")
def remove_faq(
    faq_id: UUID,
    session: Session = Depends(get_session),
):
    deleted = delete_faq(session, faq_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="FAQ not found")

    return {"message": "FAQ deleted successfully"}