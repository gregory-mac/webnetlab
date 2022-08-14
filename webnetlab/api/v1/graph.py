from fastapi import APIRouter
from fastapi.responses import RedirectResponse

from webnetlab.api.functions.graph import create_topology

router = APIRouter(prefix="/graph")


@router.get("/", response_class=RedirectResponse, status_code=200)
def root():
    return "Graphs root"


@router.get("/{lab_name}/topology", status_code=200)
def get_lab_topology(lab_name: str):
    try:
        return create_topology(lab_name)
    except Exception as e:
        return {"error": "something went wrong while trying to create lab, topology {}".format(e)}
