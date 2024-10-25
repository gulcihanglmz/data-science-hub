from fastapi import FastAPI

app = FastAPI()

strings = []

@app.get("/")
async def read_strings():
    return strings

@app.get("/lenght/")
async def string_lenght(s:str):
    strings.append(len(s))
    return {"Lenght" : len(s)}

