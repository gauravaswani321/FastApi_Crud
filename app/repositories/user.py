from sqlalchemy.orm import Session

from app import models


def get_users(db: Session) -> list[models.User]:
    return list(db.query(models.User).order_by(models.User.id.asc()).all())


def get_user(db: Session, user_id: int) -> models.User | None:
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str) -> models.User | None:
    return db.query(models.User).filter(models.User.email == email).first()


def create_user(
    db: Session,
    name: str,
    email: str,
    hashed_password: str,
    role: str = "user",
) -> models.User:
    db_user = models.User(
        name=name,
        email=email,
        hashed_password=hashed_password,
        role=role,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user(db: Session, user_id: int, update_data: dict) -> models.User | None:
    db_user = get_user(db, user_id)
    if not db_user:
        return None
    for key, value in update_data.items():
        setattr(db_user, key, value)
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(db: Session, user_id: int) -> bool:
    db_user = get_user(db, user_id)
    if not db_user:
        return False
    db.delete(db_user)
    db.commit()
    return True
