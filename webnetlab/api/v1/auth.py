from fastapi import APIRouter, Depends, HTTPException, Response, Form
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import RedirectResponse

from sqlalchemy.orm.session import Session

from core import crud
from core import schemas
from api import dependencies
from core import auth
from core import models
from core.views.auth_login import router as router_auth_login
from core.views.auth_signup import router as router_auth_register


router = APIRouter(prefix="/auth", tags=["auth"])
router.include_router(router_auth_login)
router.include_router(router_auth_register)


@router.post("/signup", response_class=RedirectResponse)
def user_signup(login=Form(), email=Form(), password=Form(), db: Session = Depends(dependencies.get_db)) -> RedirectResponse:
    new_user = schemas.UserCreate(login=login, email=email, password=password)
    user = db.query(models.user.User).filter(models.user.User.login == new_user.login).first()
    if user:
        raise HTTPException(
            status_code=400,
            detail="This user already exists in the system",
        )
    crud.user.create(db, new_user)

    return RedirectResponse(router.url_path_for("login_view"), status_code=303)


@router.post("/login", response_class=RedirectResponse)
def login(response: Response, form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(dependencies.get_db)) -> RedirectResponse:
    user = auth.authenticate(login=form_data.username, password=form_data.password, db=db)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    access_token = auth.create_access_token(sub=user.id)
    response.set_cookie(key="access_token", value=f"Bearer {access_token}", httponly=True)
    return RedirectResponse("/lab/list", status_code=303)


@router.get("/logout", response_class=RedirectResponse, status_code=303)
async def logout(response: Response):
    response.delete_cookie("access_token")
    return router.url_path_for("login_view")


@router.get("/me", response_model=schemas.User)
def user_me(current_user: models.user.User = Depends(dependencies.get_current_user)) -> models.user.User:
    return current_user
