from sqlalchemy.orm import Session

from core.models.user import User


def create(db: Session, login: str, email: str, is_admin: bool = False) -> User:
    user = User(login=login, email=email, is_admin=is_admin)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def delete(db: Session, id: int) -> User:
    user = db.query(User).get(id)
    db.delete(user)
    db.commit()
    return user
