from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from crud.policy import (
    create_policy,
    get_policies,
    get_policy_by_id,
    update_policy,
    delete_policy,
)
from database import get_session
from schemas.policy import (
    PolicyCreate,
    PolicyRead,
    PolicyUpdate,
)

router = APIRouter(
    prefix="/policies",
    tags=["Policies"],
)


@router.post("/", response_model=PolicyRead)
def create_new_policy(
    policy_data: PolicyCreate,
    session: Session = Depends(get_session),
):
    return create_policy(session, policy_data)


@router.get("/", response_model=list[PolicyRead])
def read_policies(
    session: Session = Depends(get_session),
):
    return get_policies(session)


@router.get("/{policy_id}", response_model=PolicyRead)
def read_policy(
    policy_id: UUID,
    session: Session = Depends(get_session),
):
    policy = get_policy_by_id(session, policy_id)

    if not policy:
        raise HTTPException(status_code=404, detail="Policy not found")

    return policy


@router.put("/{policy_id}", response_model=PolicyRead)
def update_existing_policy(
    policy_id: UUID,
    policy_data: PolicyUpdate,
    session: Session = Depends(get_session),
):
    policy = update_policy(
        session,
        policy_id,
        policy_data,
    )

    if not policy:
        raise HTTPException(status_code=404, detail="Policy not found")

    return policy


@router.delete("/{policy_id}")
def remove_policy(
    policy_id: UUID,
    session: Session = Depends(get_session),
):
    deleted = delete_policy(session, policy_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Policy not found")

    return {"message": "Policy deleted successfully"}