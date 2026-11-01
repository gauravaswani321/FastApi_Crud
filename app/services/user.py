from sqlalchemy.orm import Session

from app import models, repositories, schemas
from app.core import security


def get_users(db: Session) -> list[models.User]:
    return repositories.user.get_users(db)


def get_user(db: Session, user_id: int) -> models.User | None:
    return repositories.user.get_user(db, user_id)


def get_user_by_email(db: Session, email: str) -> models.User | None:
    return repositories.user.get_user_by_email(db, email)


def create_user(db: Session, user: schemas.UserCreate) -> models.User:
    hashed_pwd = security.get_password_hash(user.password)
    return repositories.user.create_user(
        db=db,
        name=user.name,
        email=user.email,
        hashed_password=hashed_pwd,
        role=user.role,
    )


def update_user(
    db: Session, user_id: int, user: schemas.UserUpdate
) -> models.User | None:
    update_data = user.model_dump(exclude_unset=True)
    return repositories.user.update_user(db, user_id, update_data)


def delete_user(db: Session, user_id: int) -> bool:
    return repositories.user.delete_user(db, user_id)
