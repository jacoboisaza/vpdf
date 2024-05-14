from sqlmodel import Session, select

from be.db.models.role import Role as Model
from be.db.models.role import RoleCreate as SchemaCreate
from be.db.models.role import RolePublic as SchemaInDB
from be.db.models.role import RoleUpdate as SchemaUpdate


class RoleCRUD:
    """Class for performing CRUD operations on the Role model."""

    def __init__(self, db: Session):
        self.db = db

    def all(self, order_by=["id"]) -> list[SchemaInDB]:
        """Return all roles sorted by the specified fields."""
        order_by = [getattr(Model, field) for field in order_by]
        return self.db.exec(select(Model).order_by(*order_by)).all()

    def create(self, obj_in: SchemaCreate) -> SchemaInDB:
        """Create a new role."""
        inserted = Model.model_validate(obj_in)
        if inserted is None:
            raise Exception("Validation error")
        self.db.add(inserted)
        self.db.commit()
        self.db.refresh(inserted)
        return inserted

    def update(self, id: int, payload: SchemaUpdate) -> SchemaInDB:
        """Update an existing role."""
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
        """Delete an existing role."""
        to_delete = self.db.get(Model, id)
        if to_delete is None:
            raise Exception(f"Item with id {id} not found")
        self.db.delete(to_delete)
        self.db.commit()
        return {"ok": True}

    def get(self, id: int) -> SchemaInDB:
        """Get a role by its ID."""
        return self.db.get(Model, id)
