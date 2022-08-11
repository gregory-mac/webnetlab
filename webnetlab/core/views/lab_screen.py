from pathlib import Path

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from api.functions.lab import get_node_information, parse_lab_specification
from core.settings import settings
from api.dependencies import templates


router = APIRouter(prefix="/open")


@router.get("/{lab_name}", status_code=200, response_class=HTMLResponse)
def open_lab_view(request: Request, lab_name: str):
    lab_details = parse_lab_specification(Path(settings.path_to_lab_files) / lab_name / settings.lab_spec_filename)
    node_info = get_node_information(lab_name)
    return templates.TemplateResponse("open_lab.html", {"request": request,
                                                        "lab_details": lab_details,
                                                        "node_info": node_info})
