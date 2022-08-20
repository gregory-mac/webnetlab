from starlette.requests import Request
from starlette.responses import HTMLResponse

from fastapi import APIRouter

from api import dependencies
from core.settings import settings


router = APIRouter()


@router.get("/login", status_code=200, response_class=HTMLResponse)
def login(request: Request):
    ip = settings.server_ip
    port = settings.server_port
    login_url = f"http://{ip}:{port}/auth/login"
    return dependencies.templates.TemplateResponse("login.html", {"request": request, "login_url": login_url})
