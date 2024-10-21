from fastapi import FastAPI

app = FastAPI()

@app.get("/")  # endpoint
async def read_root():
    return {"Hi" : "Gülcihan"}

