from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from crud.branch import (
    create_branch,
    get_branches,
    get_branch_by_id,
    update_branch,
    delete_branch,
)
from database import get_session
from schemas.branch import (
    BranchCreate,
    BranchRead,
    BranchUpdate,
)

router = APIRouter(
    prefix="/branches",
    tags=["Branches"],
)


@router.post("/", response_model=BranchRead)
def create_new_branch(
    branch_data: BranchCreate,
    session: Session = Depends(get_session),
):
    return create_branch(session, branch_data)


@router.get("/", response_model=list[BranchRead])
def read_branches(
    session: Session = Depends(get_session),
):
    return get_branches(session)


@router.get("/{branch_id}", response_model=BranchRead)
def read_branch(
    branch_id: UUID,
    session: Session = Depends(get_session),
):
    branch = get_branch_by_id(session, branch_id)

    if not branch:
        raise HTTPException(status_code=404, detail="Branch not found")

    return branch


@router.put("/{branch_id}", response_model=BranchRead)
def update_existing_branch(
    branch_id: UUID,
    branch_data: BranchUpdate,
    session: Session = Depends(get_session),
):
    branch = update_branch(
        session,
        branch_id,
        branch_data,
    )

    if not branch:
        raise HTTPException(status_code=404, detail="Branch not found")

    return branch


@router.delete("/{branch_id}")
def remove_branch(
    branch_id: UUID,
    session: Session = Depends(get_session),
):
    deleted = delete_branch(session, branch_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Branch not found")

    return {"message": "Branch deleted successfully"}