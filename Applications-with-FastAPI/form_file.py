from fastapi import FastAPI, File, UploadFile, Form
app = FastAPI()

@app.post("/upload-with-data/")
async def create_upload_with_data(
        file: UploadFile,
        description: str = Form( ... ),
        category: str = Form( ... )
):
    return {
        "filename": file.filename,
        "description": description,
        "category": category
}

