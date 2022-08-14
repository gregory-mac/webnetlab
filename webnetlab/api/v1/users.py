from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from core.crud.user import create, delete
from core.schemas.user import UserCreate, User
from api.dependencies import get_db

router = APIRouter(prefix="/users")


@router.get("/", status_code=200)
def root():
    return "Graphs root"


@router.post("/create", status_code=201, response_model=User)
def add_user(user_create: UserCreate, db: Session = Depends(get_db)) -> User:
    return create(db, user_create.login, user_create.email, user_create.is_admin)


@router.post("/delete", status_code=200, response_model=User)
def delete_user(id: int, db: Session = Depends(get_db)) -> User:
    return delete(db, id)
