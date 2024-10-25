from fastapi import FastAPI

app = FastAPI()

numbers = []

@app.get("/square/")
async def number():
    return numbers

@app.get("/square/{num}")
async def square_of_a_number(num:int):
    sqr = num**2
    numbers.append(num)
    return numbers

