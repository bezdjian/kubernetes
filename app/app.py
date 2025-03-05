from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import os

app = FastAPI()

# Get absolute path to templates directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))


@app.get("/hello")
async def hello():
    return {"message": f"Hello FastApi! from {os.environ.get('HOSTNAME', 'unknown')}"}


@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "title": "Hello FastApi!",
            "hostname": os.environ.get("HOSTNAME", "unknown"),
            "test": "This is a test message",
        },
    )
