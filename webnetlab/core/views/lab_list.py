from pathlib import Path

from starlette.requests import Request
from starlette.responses import HTMLResponse

from fastapi import APIRouter

from api import dependencies
from api import functions
from core.settings import settings


router = APIRouter(prefix="/list")


@router.get("/", status_code=200, response_class=HTMLResponse)
def list_labs_view(request: Request):
    lab_table = {}
    lab_dir_list = functions.lab.scan_for_lab_folders(settings.path_to_lab_files)
    for lab in lab_dir_list:
        lab_table[lab] = {}
        lab_details = functions.lab.parse_lab_specification(Path(settings.path_to_lab_files) / lab / settings.lab_spec_filename)
        try:
            lab_table[lab]["author"] = lab_details["author"]
        except KeyError:
            lab_table[lab]["author"] = "---"
        try:
            lab_table[lab]["difficulty"] = lab_details["difficulty"]
        except KeyError:
            lab_table[lab]["difficulty"] = "---"
    return dependencies.templates.TemplateResponse("list_labs.html", {"request": request, "lab_table": lab_table})
