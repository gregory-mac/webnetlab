from fastapi import FastAPI, Depends
from fastapi.templating import Jinja2Templates

from views.lab_screen import router as lab_screen_router


app = FastAPI(title="NetLab")
app.include_router(lab_screen_router)


@app.get("/")
def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    from uvicorn import run
    run("app:app", host="0.0.0.0", port=8080, workers=1, reload=True)
