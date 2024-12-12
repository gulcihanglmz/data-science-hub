from fastapi import  FastAPI,Depends
from fastapi.security import OAuth2PasswordRequestForm

app = FastAPI()

@app.post("/token")
async def login(
    form_data: OAuth2PasswordRequestForm = Depends()
):
    return {
        "access_token": form_data.username,
        "token_type": "bearer"
    }