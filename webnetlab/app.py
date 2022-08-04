from fastapi import FastAPI, Depends
from fastapi.templating import Jinja2Templates
from .settings import settings
from uvicorn import run

from views.lab_screen import router as lab_screen_router


def get_templates():
    return Jinja2Templates(directory="templates")


app = FastAPI(dependencies=Depends(get_templates))
app.include_router(lab_screen_router)


@app.get("/")
def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    run("app:app", host="0.0.0.0", port=8080, workers=1, reload=True)
