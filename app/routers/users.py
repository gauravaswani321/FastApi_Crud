from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import schemas, services
from app.core.database import get_db
from app.dependencies import get_current_user

router = APIRouter(prefix="/users", tags=["users"])


@router.get(
    "/", response_model=list[schemas.UserOut], dependencies=[Depends(get_current_user)]
)
def read_users(db: Session = Depends(get_db)):
    return services.user.get_users(db)


@router.get(
    "/{user_id}",
    response_model=schemas.UserOut,
    dependencies=[Depends(get_current_user)],
)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = services.user.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.post("/", response_model=schemas.UserOut, status_code=201)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    if services.user.get_user_by_email(db, user.email):
        raise HTTPException(status_code=409, detail="Email already registered")
    return services.user.create_user(db, user)


@router.put(
    "/{user_id}",
    response_model=schemas.UserOut,
    dependencies=[Depends(get_current_user)],
)
def update_user(user_id: int, user: schemas.UserUpdate, db: Session = Depends(get_db)):
    updated = services.user.update_user(db, user_id, user)
    if not updated:
        raise HTTPException(status_code=404, detail="User not found")
    return updated


@router.delete("/{user_id}", dependencies=[Depends(get_current_user)])
def delete_user(user_id: int, db: Session = Depends(get_db)):
    deleted = services.user.delete_user(db, user_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User Deleted"}
