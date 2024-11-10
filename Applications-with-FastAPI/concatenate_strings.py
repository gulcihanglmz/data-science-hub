from fastapi import FastAPI
app = FastAPI()
@app.get('/concat/')
async def concat_strings(a: str, b: str):
    return {'concatenated': a + b}

