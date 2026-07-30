from uuid import UUID

from pydantic import BaseModel


class BranchCreate(BaseModel):
    chain_id: UUID
    name: str
    address: str
    city: str
    country: str
    description: str | None = None


class BranchRead(BaseModel):
    id: UUID
    chain_id: UUID
    name: str
    address: str
    city: str
    country: str
    description: str | None = None
    is_active: bool


class BranchUpdate(BaseModel):
    chain_id: UUID | None = None
    name: str | None = None
    address: str | None = None
    city: str | None = None
    country: str | None = None
    description: str | None = None
    is_active: bool | None = None