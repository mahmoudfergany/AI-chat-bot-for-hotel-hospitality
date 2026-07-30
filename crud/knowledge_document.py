from uuid import UUID

from sqlmodel import Session, select

from models.knowledge_document import KnowledgeDocument
from schemas.knowledge_document import (
    KnowledgeDocumentCreate,
    KnowledgeDocumentUpdate,
)


def create_knowledge_document(
    session: Session,
    knowledge_document_data: KnowledgeDocumentCreate,
):

    knowledge_document = KnowledgeDocument(
        **knowledge_document_data.model_dump()
    )

    session.add(knowledge_document)
    session.commit()
    session.refresh(knowledge_document)

    return knowledge_document


def get_knowledge_documents(session: Session):

    statement = select(KnowledgeDocument)

    return session.exec(statement).all()


def get_knowledge_document_by_id(
    session: Session,
    knowledge_document_id: UUID,
):

    return session.get(
        KnowledgeDocument,
        knowledge_document_id,
    )


def update_knowledge_document(
    session: Session,
    knowledge_document_id: UUID,
    knowledge_document_data: KnowledgeDocumentUpdate,
):

    knowledge_document = session.get(
        KnowledgeDocument,
        knowledge_document_id,
    )

    if not knowledge_document:
        return None

    updates = knowledge_document_data.model_dump(
        exclude_unset=True
    )

    for key, value in updates.items():
        setattr(knowledge_document, key, value)

    session.add(knowledge_document)
    session.commit()
    session.refresh(knowledge_document)

    return knowledge_document


def delete_knowledge_document(
    session: Session,
    knowledge_document_id: UUID,
):

    knowledge_document = session.get(
        KnowledgeDocument,
        knowledge_document_id,
    )

    if not knowledge_document:
        return False

    session.delete(knowledge_document)
    session.commit()

    return True