from uuid import UUID

from sqlmodel import Session, select

from models.branch import Branch
from schemas.branch import BranchCreate, BranchUpdate


def create_branch(session: Session, branch_data: BranchCreate):

    branch = Branch(
        chain_id=branch_data.chain_id,
        name=branch_data.name,
        address=branch_data.address,
        city=branch_data.city,
        country=branch_data.country,
        description=branch_data.description,
    )

    session.add(branch)
    session.commit()
    session.refresh(branch)

    return branch


def get_branches(session: Session):

    statement = select(Branch)

    return session.exec(statement).all()


def get_branch_by_id(session: Session, branch_id: UUID):

    return session.get(Branch, branch_id)


def update_branch(
    session: Session,
    branch_id: UUID,
    branch_data: BranchUpdate,
):

    branch = session.get(Branch, branch_id)

    if not branch:
        return None

    updates = branch_data.model_dump(exclude_unset=True)

    for key, value in updates.items():
        setattr(branch, key, value)

    session.add(branch)
    session.commit()
    session.refresh(branch)

    return branch


def delete_branch(session: Session, branch_id: UUID):

    branch = session.get(Branch, branch_id)

    if not branch:
        return False

    session.delete(branch)
    session.commit()

    return True