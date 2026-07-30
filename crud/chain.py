from uuid import UUID

from sqlmodel import Session, select

from models.chain import Chain
from schemas.chain import ChainCreate, ChainUpdate

def create_chain(
    session: Session,
    chain_data: ChainCreate
):

    statement = select(Chain).where(
    Chain.name == chain_data.name
    )

    existing_chain = session.exec(statement).first()
    chain = Chain(
        name=chain_data.name,
        description=chain_data.description,
    )

    session.add(chain)
    session.commit()
    session.refresh(chain)

    return chain

def get_chains(session: Session):
    statement = select(Chain)
    chains = session.exec(statement).all()
    return chains


def get_chain_by_id(
    session: Session,
    chain_id: UUID
):
    chain = session.get(Chain, chain_id)
    return chain


def update_chain(
    session: Session,
    chain_id: UUID,
    chain_data: ChainUpdate
):
    chain = session.get(Chain, chain_id)

    if chain is None:
        return None

    chain.name = chain_data.name
    chain.description = chain_data.description
    chain.is_active = chain_data.is_active

    session.commit()
    session.refresh(chain)

    return chain


def delete_chain(
    session: Session,
    chain_id: UUID
):
    chain = session.get(Chain, chain_id)

    if chain is None:
        return None

    session.delete(chain)
    session.commit()

    return chain