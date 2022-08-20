from starlette.requests import Request
from starlette.responses import HTMLResponse

from fastapi import APIRouter

from api import dependencies
from core.settings import settings


router = APIRouter()


@router.get("/signup", status_code=200, response_class=HTMLResponse)
def signup(request: Request):
    ip = settings.server_ip
    port = settings.server_port
    signup_url = f"http://{ip}:{port}/auth/signup"
    return dependencies.templates.TemplateResponse("signup.html", {"request": request, "signup_url": signup_url})
