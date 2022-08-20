from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from core.settings import settings

from api.v1.lab import router as router_lab
from api.v1.graph import router as router_graph
from api.v1.users import router as router_users
from api.v1.auth import router as router_auth


app = FastAPI(title="NetLab")
app.include_router(router_lab)
app.include_router(router_graph)
app.include_router(router_users)
app.include_router(router_auth)
app.mount("/static", StaticFiles(directory="core/static"), name="static")


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
