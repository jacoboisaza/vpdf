from sqlmodel import Field, Relationship, SQLModel

from .role import Role
from .user_role import UserRole


class UserBase(SQLModel):
    username: str
    email: str


class User(UserBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    roles: list[Role] = Relationship(back_populates="users", link_model=UserRole)
    secret: str  # This is a secret field, it should not be exposed


class UserCreate(UserBase):
    pass


class UserPublic(UserBase):
    id: int
    roles: list[Role]


class UserUpdate(SQLModel):
    email: str | None = None
