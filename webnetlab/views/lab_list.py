from typing import List
from pathlib import Path

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from webnetlab.settings import settings
from webnetlab.dependencies import templates


router = APIRouter(prefix="/lab")


def scan_for_lab_folders(path: str) -> List[str]:
    lab_list = []
    for lab_dir in Path(path).iterdir():
        lab_list.append(str(lab_dir.name))
    return lab_list


@router.get("/", response_class=HTMLResponse)
def list_labs(request: Request):
    lab_dir_list = scan_for_lab_folders(settings.path_to_lab_files)
    return templates.TemplateResponse("lab_list.html", {"request": request, "lab_dir_list": lab_dir_list})
