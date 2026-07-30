from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from database import get_session
from crud.chain import (
    create_chain,
    get_chains,
    get_chain_by_id,
    update_chain,
    delete_chain,
)
from schemas.chain import (
    ChainCreate,
    ChainRead,
    ChainUpdate,
)

router = APIRouter(
    prefix="/chains",
    tags=["Chains"],
)


@router.post("/", response_model=ChainRead)
def create_chain_endpoint(
    chain: ChainCreate,
    session: Session = Depends(get_session),
):
    return create_chain(session, chain)


@router.get("/", response_model=list[ChainRead])
def get_chains_endpoint(
    session: Session = Depends(get_session),
):
    return get_chains(session)


@router.get("/{chain_id}", response_model=ChainRead)
def get_chain_by_id_endpoint(
    chain_id: UUID,
    session: Session = Depends(get_session),
):
    chain = get_chain_by_id(session, chain_id)

    if chain is None:
        raise HTTPException(
            status_code=404,
            detail="Chain not found",
        )

    return chain


@router.put("/{chain_id}", response_model=ChainRead)
def update_chain_endpoint(
    chain_id: UUID,
    chain: ChainUpdate,
    session: Session = Depends(get_session),
):
    updated_chain = update_chain(session, chain_id, chain)

    if updated_chain is None:
        raise HTTPException(
            status_code=404,
            detail="Chain not found",
        )

    return updated_chain


@router.delete("/{chain_id}", response_model=ChainRead)
def delete_chain_endpoint(
    chain_id: UUID,
    session: Session = Depends(get_session),
):
    deleted_chain = delete_chain(session, chain_id)

    if deleted_chain is None:
        raise HTTPException(
            status_code=404,
            detail="Chain not found",
        )

    return deleted_chain