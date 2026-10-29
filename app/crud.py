from sqlalchemy.orm import Session
from app import models, schemas, security

def authenticate_user(db: Session, email: str, password: str) -> models.User:
    user = get_user_by_email(db, email)
    if not user or not user.hashed_password:
        return False
    if not security.verify_password(password, str(user.hashed_password)):
        return False
    return user

def get_users(db: Session) -> list[models.User]:
    return db.query(models.User).all()

def get_user(db: Session, user_id: int) -> models.User | None:
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_email(db: Session, email:str) -> models.User | None:
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, user: schemas.UserCreate) -> models.User:
    hashed_pwd = security.get_password_hash(user.password)
    # db_user = models.User(**user.model_dump())
    db_user = models.User(
        name=user.name,
        email=user.email,
        hashed_password=hashed_pwd,
        role=user.role,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, user_id: int, user: schemas.UserUpdate) -> models.User | None:
    db_user = get_user(db, user_id)
    if not db_user:
        return None
    for key, value in user.model_dump(exclude_unset=True).items():
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