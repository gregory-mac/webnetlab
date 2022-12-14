from fastapi import FastAPI, Depends, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from fastapi.exception_handlers import http_exception_handler
from starlette.exceptions import HTTPException as StarletteHTTPException

from api import dependencies
from api.v1.lab import router as router_lab
from api.v1.graph import router as router_graph
from api.v1.users import router as router_users
from api.v1.auth import router as router_auth
from core.settings import settings


app = FastAPI(title="NetLab")
app.include_router(router_lab, dependencies=[Depends(dependencies.get_current_user)])
app.include_router(router_graph, dependencies=[Depends(dependencies.get_current_user)])
app.include_router(router_users, dependencies=[Depends(dependencies.get_current_user)])
app.include_router(router_auth)
app.mount("/static", StaticFiles(directory="core/static"), name="static")


@app.get("/", response_class=RedirectResponse)
def root() -> RedirectResponse:
    return RedirectResponse(app.url_path_for("login"), status_code=303)


@app.exception_handler(StarletteHTTPException)
async def redirect_common_exceptions(request: Request, exc: StarletteHTTPException):
    if exc.status_code == 401:
        return dependencies.templates.TemplateResponse("errors/401.html", {"request": request})
    elif exc.status_code == 404:
        return dependencies.templates.TemplateResponse("errors/404.html", {"request": request})
    elif exc.status_code == 500:
        return dependencies.templates.TemplateResponse("errors/500.html", {"request": request})
    else:
        return await http_exception_handler(request, exc)


if __name__ == "__main__":
    from uvicorn import run
    run("app:app",
        host=settings.server_ip,
        port=settings.server_port,
        workers=settings.worker_count,
        reload=settings.reload_app_on_change,
        )
