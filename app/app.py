from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import os
from pymongo import MongoClient

app = FastAPI()

# Get absolute path to templates directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))


@app.get("/hello")
async def hello():
    # get data from mongodb
    mongodb_url = os.environ.get("MONGODB_URL", "mongodb://localhost:27017/")
    print(f"MONGODB_URL: {mongodb_url}")
    if mongodb_url.__contains__("localhost"):
        client = MongoClient(mongodb_url)
    else:
        mongodb_user = os.environ.get("MONGODB_USER")
        mongodb_pass = os.environ.get("MONGODB_PASSWORD")
        url = f"mongodb://{mongodb_user}:{mongodb_pass}@{mongodb_url}"
        client = MongoClient(url)
        print(f"Formatted URL: {url}")
    
    db = client["test"]
    collection = db["test"]
    data = []
    for c in collection.find({}):
        data.append(c["name"])

    return {
        "message": f"Hello FastApi! from {os.environ.get('HOSTNAME', 'unknown')}", 
        "names": data
        }


@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "title": "Hello FastApi!",
            "hostname": os.environ.get("HOSTNAME", "unknown"),
            "mongodb_url": os.environ.get("MONGODB_URL", "unknown"),
            "test": "This is a test message",
        },
    )
