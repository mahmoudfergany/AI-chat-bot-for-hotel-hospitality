from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from crud.knowledge_document import (
    create_knowledge_document,
    get_knowledge_documents,
    get_knowledge_document_by_id,
    update_knowledge_document,
    delete_knowledge_document,
)

from database import get_session

from schemas.knowledge_document import (
    KnowledgeDocumentCreate,
    KnowledgeDocumentRead,
    KnowledgeDocumentUpdate,
)

router = APIRouter(
    prefix="/knowledge-documents",
    tags=["Knowledge Documents"],
)


@router.post("/", response_model=KnowledgeDocumentRead)
def create_new_knowledge_document(
    knowledge_document_data: KnowledgeDocumentCreate,
    session: Session = Depends(get_session),
):
    return create_knowledge_document(session, knowledge_document_data)


@router.get("/", response_model=list[KnowledgeDocumentRead])
def read_knowledge_documents(
    session: Session = Depends(get_session),
):
    return get_knowledge_documents(session)


@router.get("/{knowledge_document_id}", response_model=KnowledgeDocumentRead)
def read_knowledge_document(
    knowledge_document_id: UUID,
    session: Session = Depends(get_session),
):
    knowledge_document = get_knowledge_document_by_id(
        session,
        knowledge_document_id,
    )

    if not knowledge_document:
        raise HTTPException(
            status_code=404,
            detail="Knowledge document not found",
        )

    return knowledge_document


@router.put("/{knowledge_document_id}", response_model=KnowledgeDocumentRead)
def update_existing_knowledge_document(
    knowledge_document_id: UUID,
    knowledge_document_data: KnowledgeDocumentUpdate,
    session: Session = Depends(get_session),
):
    knowledge_document = update_knowledge_document(
        session,
        knowledge_document_id,
        knowledge_document_data,
    )

    if not knowledge_document:
        raise HTTPException(
            status_code=404,
            detail="Knowledge document not found",
        )

    return knowledge_document


@router.delete("/{knowledge_document_id}")
def remove_knowledge_document(
    knowledge_document_id: UUID,
    session: Session = Depends(get_session),
):
    deleted = delete_knowledge_document(
        session,
        knowledge_document_id,
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Knowledge document not found",
        )

    return {
        "message": "Knowledge document deleted successfully"
    }