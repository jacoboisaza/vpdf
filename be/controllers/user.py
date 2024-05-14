from sqlmodel import Session, select

from be.db.models.role import Role as RoleModel
from be.db.models.user import User as Model
from be.db.models.user import UserCreate as SchemaCreate
from be.db.models.user import UserPublic as SchemaInDB
from be.db.models.user import UserUpdate as SchemaUpdate


class UserCRUD:
    """Class for performing CRUD operations on User objects."""

    def __init__(self, db: Session):
        self.db = db

    def all(self, order_by=["id"]) -> list[SchemaInDB]:
        """Return all User objects sorted by the specified fields."""
        order_by = [getattr(Model, field) for field in order_by]
        return self.db.exec(select(Model).order_by(*order_by)).all()

    def create(self, obj_in: SchemaCreate) -> SchemaInDB:
        """Create a new User object."""
        inserted = Model.model_validate(obj_in)
        if inserted is None:
            raise Exception("Validation error")
        self.db.add(inserted)
        self.db.commit()
        self.db.refresh(inserted)
        return inserted

    def update(self, id: int, payload: SchemaUpdate) -> SchemaInDB:
        """Update an existing User object."""
        updated = self.db.get(Model, id)
        if updated is None:
            raise Exception(f"Item with id {id} not found")
        db_item = payload.model_dump(exclude_unset=True)
        updated.sqlmodel_update(db_item)
        self.db.add(updated)
        self.db.commit()
        self.db.refresh(updated)
        return updated

    def delete(self, id: int) -> dict[str, bool]:
        """Delete an existing User object."""
        to_delete = self.db.get(Model, id)
        if to_delete is None:
            raise Exception(f"Item with id {id} not found")
        self.db.delete(to_delete)
        self.db.commit()
        return {"ok": True}

    def get(self, id: int) -> SchemaInDB:
        """Get a User object by ID."""
        return self.db.get(Model, id)

    def add_role(self, user_id: int, role_id: int) -> SchemaInDB:
        """Add a role to a User object."""
        user = self.db.get(Model, user_id)
        role = self.db.get(RoleModel, role_id)
        user.roles.append(role)
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user
