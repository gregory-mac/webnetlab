from starlette.requests import Request
from starlette.responses import HTMLResponse

from fastapi import APIRouter

from api import dependencies
from api import functions
from core.settings import settings


router = APIRouter(prefix="/list")


@router.get("/", status_code=200, response_class=HTMLResponse)
def list_labs_view(request: Request):
    lab_dir_list = functions.lab.scan_for_lab_folders(settings.path_to_lab_files)
    return dependencies.templates.TemplateResponse("list_labs.html", {"request": request, "lab_dir_list": lab_dir_list})
