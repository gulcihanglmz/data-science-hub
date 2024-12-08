from fastapi import FastAPI, File, UploadFile

app = FastAPI()
@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    content = await file.read()
    print(content)
    return {
        "filename": file.filename,
        "content_type": file.content_type
    }
