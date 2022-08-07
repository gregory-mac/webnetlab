from fastapi import FastAPI, Depends
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from webnetlab.settings import settings

from views.lab_screen import router as lab_screen_router


app = FastAPI(title="NetLab")
app.include_router(lab_screen_router)
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    from uvicorn import run
    run("app:app",
        host=settings.server_ip,
        port=settings.server_port,
        workers=settings.worker_count,
        reload=settings.reload_app_on_change,
        )
