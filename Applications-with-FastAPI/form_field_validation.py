from pydantic import EmailStr
from fastapi import FastAPI,Form

app = FastAPI()

@app.post("/register/")
async def register(
    email: EmailStr = Form(...),
    password: str = Form(..., min_length=8),
    age: int = Form(..., gt=0, lt=120)
):
    return {"message": "Registration successful"}
