from sqlalchemy.orm import Session

from core import models, schemas, auth


def create(db: Session, new_user: schemas.UserCreate) -> models.user.User:
    create_data = new_user.dict()
    create_data.pop("password")
    new_user_in_db = models.user.User(**create_data)
    new_user_in_db.hashed_password = auth.get_password_hash(new_user.password)
    db.add(new_user_in_db)
    db.commit()
    db.refresh(new_user_in_db)

    return new_user_in_db


def delete(db: Session, id: int) -> models.user.User:
    user = db.query(models.user.User).get(id)
    db.delete(user)
    db.commit()
    return user
