from fastapi import FastAPI,File,Form, UploadFile

app = FastAPI()
@app.post("/upload/")
async def upload_file(
    file: UploadFile = File(...),
    description: str = Form(...)
):
    return {
        "filename": file.filename,
        "description": description
    }


# Form with Optional Fields
@app.post("/profile/")
async def update_profile_optional(
    username: str = Form(...),
    bio: str = Form(None),
    website: str = Form(None),
    age: int = Form(None)
):
    return {
        "username": username,
        "bio": bio,
        "website": website,
        "age": age
    }