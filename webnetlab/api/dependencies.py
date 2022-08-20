from typing import Generator, Optional
from pydantic import BaseModel

from sqlalchemy.orm.session import Session

from fastapi import Depends, HTTPException, status
from fastapi.templating import Jinja2Templates

from jose import jwt, JWTError

from core import auth
from core import models
from core.settings import settings
from core.db.session import session


templates = Jinja2Templates(directory="core/templates")


def get_db() -> Generator:
    with session() as db:
        db.current_user_id = None
        yield db


class TokenData(BaseModel):
    username: Optional[str] = None


def get_current_user(db: Session = Depends(get_db), token: str = Depends(auth.oauth2_scheme)) -> models.user.User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(
            token,
            settings.jwt_secret,
            algorithms=[settings.jwt_algorithm],
            options={"verify_aud": False},
        )
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception

    user = db.query(models.user.User).filter(models.user.User.id == token_data.username).first()
    if user is None:
        raise credentials_exception
    return user
