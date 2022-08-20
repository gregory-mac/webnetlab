from typing import Optional, MutableMapping, List, Union
from datetime import datetime, timedelta

from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm.session import Session
from jose import jwt

from core import models
from core import auth
from core.settings import settings


JWTPayloadMapping = MutableMapping[
    str, Union[datetime, bool, str, List[str], List[int]]
]

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


def authenticate(login: str, password: str, db: Session) -> Optional[models.user.User]:
    user = db.query(models.user.User).filter(models.user.User.login == login).first()
    if not user:
        return None
    if not auth.verify_password(password, user.hashed_password):
        return None
    return user


def create_access_token(sub: str) -> str:
    return _create_token(
        token_type="access_token",
        lifetime=timedelta(minutes=settings.jwt_token_expiry),
        sub=sub,
    )


def _create_token(token_type: str, lifetime: timedelta, sub: str,) -> str:
    payload = {}
    expire = datetime.utcnow() + lifetime
    payload["type"] = token_type
    payload["exp"] = expire
    payload["iat"] = datetime.utcnow()
    payload["sub"] = str(sub)

    return jwt.encode(payload, settings.jwt_secret, algorithm=settings.jwt_algorithm)
