from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "message": "Привет, введи своё имя"})

@app.post("/greet/", response_class=HTMLResponse)
async def greet_user(request: Request, name: str = Form(...)):
    return templates.TemplateResponse("greet.html", {"request": request, "message": f"Привет, {name}!"})
