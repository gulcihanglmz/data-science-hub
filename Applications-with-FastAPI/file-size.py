from fastapi import FastAPI, UploadFile

app = FastAPI()

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    content = await file.read()  # Read file content
    return {"file_size": len(content)}
