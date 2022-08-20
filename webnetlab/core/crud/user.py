from sqlalchemy.orm import Session

from core import models


def create(db: Session, login: str, email: str, is_admin: bool = False) -> models.user.User:
    user = models.user.User(login=login, email=email, is_admin=is_admin)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def delete(db: Session, id: int) -> models.user.User:
    user = db.query(models.user.User).get(id)
    db.delete(user)
    db.commit()
    return user
