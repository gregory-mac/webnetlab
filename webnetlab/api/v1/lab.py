from fastapi import APIRouter
from fastapi.responses import RedirectResponse

from api.functions import lab
from core.settings import settings
from core.views.lab_screen import router as router_lab_screen
from core.views.lab_list import router as router_lab_list


router = APIRouter(prefix="/lab", tags=["lab"])
router.include_router(router_lab_screen)
router.include_router(router_lab_list)


@router.get("/", response_class=RedirectResponse, status_code=303)
def root():
    return router.url_path_for("list_labs_view")


@router.post("/status", status_code=200)
def check_lab_status():
    return lab.check_status()


@router.post("/{lab_name}/deploy", status_code=200)
def deploy_lab_button(lab_name: str):
    path_to_clab_yaml = f"{settings.path_to_lab_files}{lab_name}/{lab_name}.clab.yml"
    try:
        lab.deploy_lab(path_to_clab_yaml)
        return {"success": "lab is deployed"}
    except Exception as e:
        return {"error": "something went wrong during the deployment process, {}".format(e)}


@router.post("/{lab_name}/destroy", status_code=200)
def destroy_lab_button(lab_name: str):
    path_to_clab_yaml = f"{settings.path_to_lab_files}{lab_name}/{lab_name}.clab.yml"
    try:
        lab.destroy_lab(path_to_clab_yaml)
        return {"success": "lab is destroyed"}
    except Exception as e:
        return {"error": "something went wrong during destruction process, {}".format(e)}
