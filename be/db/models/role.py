from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship, SQLModel

from .user_role import UserRole

# Handle circular imports
if TYPE_CHECKING:
    from .user import User


class RoleBase(SQLModel):
    name: str


class Role(RoleBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    users: list["User"] = Relationship(back_populates="roles", link_model=UserRole)


class RoleCreate(RoleBase):
    pass


class RolePublic(RoleBase):
    id: int
    name: str


class RoleUpdate(SQLModel):
    name: str
