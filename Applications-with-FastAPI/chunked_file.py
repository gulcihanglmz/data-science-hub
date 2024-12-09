from fastapi import FastAPI, UploadFile

app = FastAPI()

# Chunked reading for large files
@app.post("/upload-chunked/")
async def upload_chunked(file: UploadFile):
  CHUNK_SIZE = 1024  # 1KB chunks
  contents = []
  while chunk := await file.read(CHUNK_SIZE):
      contents.append(chunk)
  return {"chunks_received": len(contents)}

# CHUNK_SIZE değişkeni, dosyanın parçalar (chunk) halinde okunacağını belirtir
# ve her seferinde ne kadar veri okunacağını belirler.

'''
Burada chunk değişkenine, file.read(CHUNK_SIZE) fonksiyonunun döndürdüğü değer atanıyor 
ve aynı anda bu değer while döngüsünde kontrol ediliyor.
variable := expression 
'''