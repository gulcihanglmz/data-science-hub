from fastapi import FastAPI, UploadFile, HTTPException

app = FastAPI()

@app.post("/upload/")
async def upload_file(file: UploadFile):
    try:
        content = await file.read()

        # Size validation
        if len(content) > 5_000_000:  # 5MB limit
            raise HTTPException(status_code=400, detail="File too large")

        # Process the content
        file_location = f"{file.filename}"
        with open(file_location, "wb") as f:
            f.write(content)

        return {
            "filename": file.filename,
            "size": len(content),
            "content_type": file.content_type,
            "location": file_location
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        await file.close()
