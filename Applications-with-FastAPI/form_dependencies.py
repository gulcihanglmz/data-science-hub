from fastapi import Depends
from fastapi import FastAPI,Form

app = FastAPI()

async def verify_token(token: str = Form(...)):
    return token

@app.post("/protected/")
async def protected_route(
    message: str = Form(...),
    token: str = Depends(verify_token)
):
    return {"message": message}
