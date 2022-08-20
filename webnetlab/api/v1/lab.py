from core.settings import settings
from api.functions.lab import deploy_lab, destroy_lab
from fastapi import APIRouter, Depends
from fastapi.responses import RedirectResponse

from api import dependencies
from core.views.lab_screen import router as router_lab_screen
from core.views.lab_list import router as router_lab_list


router = APIRouter(prefix="/lab", tags=["lab"], dependencies=[Depends(dependencies.get_current_user)])
router.include_router(router_lab_screen)
router.include_router(router_lab_list)

DEPLOYED_LAB = False
DEPLOYED_LAB_NAME = ""


@router.get("/", response_class=RedirectResponse, status_code=303)
def root():
    return router.url_path_for("list_labs_view")


@router.post("/status", status_code=200)
def check_lab_status():
    global DEPLOYED_LAB
    global DEPLOYED_LAB_NAME
    status = {"is_running": DEPLOYED_LAB,
              "lab_name": DEPLOYED_LAB_NAME}
    return status


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
