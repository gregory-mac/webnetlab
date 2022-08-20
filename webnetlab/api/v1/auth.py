from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from sqlalchemy.orm.session import Session

from core import crud
from core import schemas
from api import dependencies
from core import auth
from core import models


router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/signup", response_model=schemas.User, status_code=201)
def user_signup(new_user: schemas.user.UserCreate, db: Session = Depends(dependencies.get_db)) -> HTTPException or models.user.User:
    user = db.query(models.user.User).filter(models.user.User.login == new_user.login).first()
    if user:
        raise HTTPException(
            status_code=400,
            detail="This user already exists in the system",
        )
    user = crud.user.create(db, new_user)

    return user


@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(dependencies.get_db)) -> HTTPException or dict:
    user = auth.authenticate(login=form_data.username, password=form_data.password, db=db)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    return {
        "access_token": auth.create_access_token(sub=user.id),
        "token_type": "bearer",
    }


@router.get("/me", response_model=schemas.User)
def user_me(current_user: models.user.User = Depends(dependencies.get_current_user)) -> models.user.User:
    return current_user
