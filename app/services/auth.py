from sqlalchemy.orm import Session

from app import models, repositories
from app.core import security


def authenticate_user(db: Session, email: str, password: str) -> models.User | None:
    user = repositories.user.get_user_by_email(db, email)
    if not user or not user.hashed_password:
        return None
    if not security.verify_password(password, str(user.hashed_password)):
        return None
    return user


def create_access_token(user: models.User) -> str:
    return security.create_access_token(data={"sub": user.email, "role": user.role})

