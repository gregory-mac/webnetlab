from typing import List
from pathlib import Path
import yaml
import subprocess

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from webnetlab.settings import settings
from webnetlab.dependencies import templates


router = APIRouter(prefix="/lab")

DEPLOYED_LAB = False
DEPLOYED_LAB_NAME = ""


def scan_for_lab_folders(path: str) -> List[str]:
    lab_list = []
    for lab_dir in Path(path).iterdir():
        if Path.is_dir(lab_dir):
            lab_list.append(str(lab_dir.name))
    return lab_list


def parse_lab_specification(lab_spec_filename: str) -> dict:
    try:
        return yaml.safe_load(Path(lab_spec_filename).read_text())
    except yaml.YAMLError as e:
        return {"error": "Could not parse lab specification file, {}".format(e)}
    except FileNotFoundError as e:
        return {"error": "Could not find lab specification file, {}".format(e)}


def get_node_information(lab_name: str) -> dict:
    path_to_clab_yaml = f"{settings.path_to_lab_files}{lab_name}/{lab_name}.clab.yml"

    try:
        configuration = yaml.safe_load(Path(path_to_clab_yaml).read_text())
    except yaml.YAMLError as e:
        return {"error": "Could not parse lab configuration file, {}".format(e)}

    node_info = {}

    try:
        for node in configuration["topology"]["nodes"]:
            node_info[node] = {}
            node_info[node]["mgmt_ip"] = configuration["topology"]["nodes"][node]["mgmt_ipv4"]
            node_info[node]["kind"] = configuration["topology"]["nodes"][node]["kind"]
            node_info[node]["image"] = configuration["topology"]["nodes"][node]["image"]
        return node_info
    except KeyError:
        pass


def deploy_lab(clab_yml: str):
    cmd = f"sudo containerlab deploy --reconfigure -t {clab_yml}"
    subprocess.run(cmd.split())


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


# @router.post("/{lab_name}/deploy", status_code=200)
# def deploy_lab_button(lab_name: str):
#     path_to_clab_yaml = f"{settings.path_to_lab_files}{lab_name}/{lab_name}.clab.yml"
#     deploy_lab(path_to_clab_yaml)
#     return {"success": "lab is deployed"}


@router.post("/{lab_name}/deploy", status_code=200)
def deploy_lab_button(lab_name: str):
    global DEPLOYED_LAB
    global DEPLOYED_LAB_NAME

    from time import sleep
    try:
        sleep(2)
        DEPLOYED_LAB = True
        DEPLOYED_LAB_NAME = lab_name
        return {"success": "lab is deployed"}
    except Exception as e:
        return {"error": "something went wrong during the deployment process, {}".format(e)}


@router.post("/{lab_name}/destroy", status_code=200)
def destroy_lab_button(lab_name: str):
    global DEPLOYED_LAB
    global DEPLOYED_LAB_NAME

    from time import sleep
    try:
        sleep(2)
        DEPLOYED_LAB = False
        DEPLOYED_LAB_NAME = ""
        return {"success": "lab is destroyed"}
    except Exception as e:
        return {"error": "something went wrong while stopping the lab, {}".format(e)}


@router.post("/status", status_code=200)
def check_lab_status():
    global DEPLOYED_LAB
    global DEPLOYED_LAB_NAME
    status = {"is_running": DEPLOYED_LAB,
              "lab_name": DEPLOYED_LAB_NAME}
    return status
