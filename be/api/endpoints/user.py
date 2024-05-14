import traceback

from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session

from be.controllers.user import UserCRUD as crud
from be.db.models.user import UserCreate as SchemaCreate
from be.db.models.user import UserPublic as SchemaOut
from be.db.models.user import UserUpdate as SchemaUpdate
from be.db.session import get_session

user_router = APIRouter(
    prefix="/user",
    tags=["User"],
)
router = user_router


@router.get("/", response_model=list[SchemaOut])
def all(db: Session = Depends(get_session)):
    """Return all."""
    try:
        return crud(db=db).all()
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=[{"msg": f"Not found because: {str(e)}"}],
        )


@router.post("/", status_code=201)
def create(
    obj_in: SchemaCreate | list[SchemaCreate],
    db: Session = Depends(get_session),
):
    """Create one or many."""
    try:
        count = 0
        created_ids = []
        if not isinstance(obj_in, list):
            obj_in = [obj_in]
        for obj in obj_in:
            try:
                new_user = crud(db=db).create(obj)
                count += 1
                created_ids.append(new_user.id)
            except Exception:
                pass
        return {
            "not_processed": len(obj_in) - count,
            "created": count,
            "created_ids": created_ids,
        }
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=[{"msg": f"Not created because: {str(e)}"}],
        )


@router.put("/{id}", response_model=SchemaOut, status_code=202)
async def update(
    id: int,
    payload: SchemaUpdate,
    db: Session = Depends(get_session),
):
    """Update an existing one."""
    try:
        return crud(db=db).update(payload=payload, id=id)
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=[{"msg": f"Not updated because: {str(e)}"}],
        )


@router.delete("/{id}", status_code=204)
def delete(id: int, db: Session = Depends(get_session)):
    """Delete an existing one."""
    try:
        return crud(db=db).delete(id)
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=[{"msg": f"Not deleted because: {str(e)}"}],
        )


@router.post("/{user_id}/role/{role_id}", response_model=SchemaOut, status_code=201)
def add_role(
    user_id: int,
    role_id: int,
    db: Session = Depends(get_session),
):
    """Add role to user."""
    try:
        return crud(db).add_role(user_id=user_id, role_id=role_id)
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=[{"msg": f"Not added because: {str(e)}"}],
        )


@router.get("/{id}", response_model=SchemaOut)
def get(id: int, db: Session = Depends(get_session)):
    """Get by id."""
    try:
        return crud(db=db).get(id)
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=[{"msg": f"Not found because: {str(e)}"}],
        )
