from pathlib import Path

from fastapi import Request
from fastapi.responses import HTMLResponse

from api.functions.lab import get_node_information, parse_lab_specification, scan_for_lab_folders
from core.settings import settings
from api.dependencies import templates
from api.v1.lab import router


@router.get("/", status_code=200, response_class=HTMLResponse)
def list_labs_view(request: Request):
    lab_dir_list = scan_for_lab_folders(settings.path_to_lab_files)
    return templates.TemplateResponse("list_labs.html", {"request": request, "lab_dir_list": lab_dir_list})


@router.get("/{lab_name}", status_code=200, response_class=HTMLResponse)
def open_lab_view(request: Request, lab_name: str):
    lab_details = parse_lab_specification(Path(settings.path_to_lab_files) / lab_name / settings.lab_spec_filename)
    node_info = get_node_information(lab_name)
    return templates.TemplateResponse("open_lab.html", {"request": request,
                                                        "lab_details": lab_details,
                                                        "node_info": node_info})
