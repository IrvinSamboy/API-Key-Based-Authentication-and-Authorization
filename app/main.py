from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def indeX():
    return {"message": "Server running"}