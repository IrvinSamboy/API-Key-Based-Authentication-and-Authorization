from fastapi import FastAPI, Request
from app.db.db import db
from app.middlewares.validate_api_key import validate_api_key

app = FastAPI()


@validate_api_key.get('/return_welcome_message')
async def index(request : Request):
    app_name = request.headers["Application-Name"]
    if app_name == "App 1":
        return {"message": "hi app 1"}
    if app_name == "App 2":
        return {"message": "hi app 2"}
    if app_name == "App 3":
        return {"message": "hi app 3"}
        
app.mount("/", validate_api_key)

@app.get('/')
async def indeX():
    return {"message": "hi"}