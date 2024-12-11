from datetime import date
from enum import Enum
from fastapi import FastAPI,Form

app = FastAPI()

class UserType(str, Enum):
    ADMIN = "admin"
    USER = "user"

@app.post("/create-event/")
async def create_event(
    event_date: date = Form(...),
    user_type: UserType = Form(...),
    description: str = Form(...)
):
    return {"event": "created"}
