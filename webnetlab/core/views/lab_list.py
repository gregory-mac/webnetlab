from starlette.requests import Request
from starlette.responses import HTMLResponse

from fastapi import APIRouter

from api.dependencies import templates
from api.functions.lab import scan_for_lab_folders
from core.settings import settings


router = APIRouter(prefix="/list")


@router.get("/lab-list", status_code=200, response_class=HTMLResponse)
def list_labs_view(request: Request):
    lab_dir_list = scan_for_lab_folders(settings.path_to_lab_files)
    return templates.TemplateResponse("list_labs.html", {"request": request, "lab_dir_list": lab_dir_list})
