from uuid import UUID

from sqlmodel import Session, select

from models.policy import Policy
from schemas.policy import (
    PolicyCreate,
    PolicyUpdate,
)


def create_policy(session: Session, policy_data: PolicyCreate):

    policy = Policy(**policy_data.model_dump())

    session.add(policy)
    session.commit()
    session.refresh(policy)

    return policy


def get_policies(session: Session):

    statement = select(Policy)

    return session.exec(statement).all()


def get_policy_by_id(session: Session, policy_id: UUID):

    return session.get(Policy, policy_id)


def update_policy(
    session: Session,
    policy_id: UUID,
    policy_data: PolicyUpdate,
):

    policy = session.get(Policy, policy_id)

    if not policy:
        return None

    updates = policy_data.model_dump(exclude_unset=True)

    for key, value in updates.items():
        setattr(policy, key, value)

    session.add(policy)
    session.commit()
    session.refresh(policy)

    return policy


def delete_policy(session: Session, policy_id: UUID):

    policy = session.get(Policy, policy_id)

    if not policy:
        return False

    session.delete(policy)
    session.commit()

    return True