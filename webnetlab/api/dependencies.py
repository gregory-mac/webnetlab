from typing import Generator
from fastapi.templating import Jinja2Templates

from core.db.session import session

templates = Jinja2Templates(directory="core/templates")


def get_db() -> Generator:
    with session() as db:
        db.current_user_id = None
        yield db
