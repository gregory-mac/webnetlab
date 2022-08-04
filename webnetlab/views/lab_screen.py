from fastapi import APIRouter


router = APIRouter(prefix="/lab")


@router.get("/")
def root():
    return {"message": "Hello World"}
