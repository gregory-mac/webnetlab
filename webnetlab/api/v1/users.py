from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from core import crud
from core import schemas
from api import dependencies

router = APIRouter(prefix="/users")


@router.get("/", status_code=200)
def root():
    return "Graphs root"


@router.post("/create", status_code=201, response_model=schemas.User)
def add_user(user_create: schemas.UserCreate, db: Session = Depends(dependencies.get_db)) -> schemas.User:
    return crud.create(db, user_create)


@router.post("/delete", status_code=200, response_model=schemas.User)
def delete_user(id: int, db: Session = Depends(dependencies.get_db)) -> schemas.User:
    return crud.delete(db, id)
