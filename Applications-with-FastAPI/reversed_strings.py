from fastapi import FastAPI

app = FastAPI()

@app.get('/reverse/')
async def reverse_string(s: str):
    return {'reversed': s[:3:-1]}

