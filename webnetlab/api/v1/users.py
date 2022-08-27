from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from api import dependencies
from core import crud, schemas


router = APIRouter(prefix="/users", tags=["users"])


@router.post("/create", status_code=201, response_model=schemas.User)
def add_user(user_create: schemas.UserCreate, db: Session = Depends(dependencies.get_db)) -> schemas.User:
    return crud.create(db, user_create)


@router.post("/delete", status_code=200, response_model=schemas.User)
def delete_user(id: int, db: Session = Depends(dependencies.get_db)) -> schemas.User:
    return crud.delete(db, id)
