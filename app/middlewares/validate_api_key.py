from fastapi import FastAPI, Request
from app.db.db import db
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from starlette.datastructures import MutableHeaders

validate_api_key = FastAPI()

@validate_api_key.middleware('http')
async def index(request: Request, call_next):
    if "apiKey" in request.headers:
        apiKey = request.headers["apiKey"]
        new_header = MutableHeaders(request._headers)
        
        app_data = next((item for item in db if item["aplicationKey"] == apiKey), None)
        
        if app_data:
            new_header["Application-Name"] = app_data["aplicationName"]
            response = await call_next(request)
            return response
        else: 
            return JSONResponse(content=jsonable_encoder("¡ERROR! invalid api key"))