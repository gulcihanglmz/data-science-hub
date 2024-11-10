from fastapi import FastAPI, HTTPException

app = FastAPI()

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

@app.get("/prime/{num}")
async def prime(num: int):
    if num < 1:
        raise HTTPException(status_code=400, detail="Input must be greater than 0.")
    return {"is_prime": is_prime(num)}

