from os import environ

from pydantic import PostgresDsn
from sqlmodel import Session, create_engine

from .models.role import Role
from .models.user import User
from .models.user_role import UserRole

models = [User, Role, UserRole]

POSTGRES_DATABASE_URL = PostgresDsn.build(
    scheme="postgresql",
    username=environ.get("DB_USERNAME"),
    password=environ.get("DB_PASSWORD"),
    host=environ.get("DB_HOST", "error_host_not_set"),
    path=environ.get("DB_NAME"),
    port=int(environ.get("DB_PORT", 5432)),
)

engine = create_engine(str(POSTGRES_DATABASE_URL))


def get_session():
    """Session generator."""
    with Session(engine) as session:
        yield session
