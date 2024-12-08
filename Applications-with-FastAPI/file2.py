from fastapi import HTTPException
from fastapi import FastAPI,  UploadFile

app = FastAPI()

@app.post("/fileSize/")
async def validate_file_size(file: UploadFile, max_size: int):
    content = await file.read()
    if len(content) > max_size:
        raise HTTPException(400, "File too large")
    return content


