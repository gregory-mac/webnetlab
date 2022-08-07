from parser import ParserError
from typing import List
from pathlib import Path
import yaml
import subprocess

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from webnetlab.settings import settings
from webnetlab.dependencies import templates


router = APIRouter(prefix="/lab")


def scan_for_lab_folders(path: Path) -> List[str]:
    lab_list = []
    for lab_dir in path.iterdir():
        lab_list.append(str(lab_dir.name))
    return lab_list


def parse_lab_specification(lab_spec_filename: str) -> dict:
    try:
        return yaml.safe_load(Path(lab_spec_filename).read_text())
    except ParserError:
        return {"Error": "Could not parse lab specification file"}
    except FileNotFoundError:
        return {"Error": "Could not find lab specification file"}


def deploy_lab(clab_yml: str):
    cmd = f"sudo containerlab deploy --reconfigure -t {clab_yml}"
    subprocess.run(cmd.split())


@router.get("/", status_code=200, response_class=HTMLResponse)
def list_labs_view(request: Request):
    lab_dir_list = scan_for_lab_folders(settings.path_to_lab_files)
    return templates.TemplateResponse("list_labs.html", {"request": request, "lab_dir_list": lab_dir_list})


@router.get("/{lab_name}", status_code=200, response_class=HTMLResponse)
def open_lab_view(request: Request, lab_name: str):
    lab_details = parse_lab_specification(settings.path_to_lab_files / lab_name / settings.lab_spec_filename)
    return templates.TemplateResponse("open_lab.html", {"request": request, "lab_details": lab_details})


@router.post("/{lab_name}/deploy", status_code=200)
def deploy_lab_button(request: Request, lab_name: str):
    path_to_clab_yaml = f"{lab_name}.clab.yml"
    deploy_lab(path_to_clab_yaml)
    return {"success": "lab is deployed"}
