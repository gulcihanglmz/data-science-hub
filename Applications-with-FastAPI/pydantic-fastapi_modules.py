from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import Form
from fastapi import File,UploadFile
from fastapi import HTTPException
from fastapi import Depends
from fastapi import BackgroundTasks
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer
from fastapi import WebSocket

app = FastAPI()

class Student(BaseModel):
    id: int
    name: str
    grade: int


# Form Data
@app.post("/login")
async def login(name: str = Form(), id: int = Form()):
    return {"Name": name, "ID": id}


# File Uploads
@app.post("/uploadfile/")
def create_upload_file(file: UploadFile = File(...)):
    return {"FileName" : file.filename}


# Handling Errors
@app.get("/items/{itemid}")
async def read_item(itemid: int):
    if itemid == 0:
        raise HTTPException(status_code=404 , detail="item not found")
    return {"item_id" : itemid}


# Dependency Injection
def common_parameters(q: str = None):
    return {"q" : q}

@app.get("/items/")
async def read_items(commons : dict = Depends(common_parameters())):
    return commons


# Background Tasks
def write_log(log_message: str):
    with open("log.txt", "a") as log_file:
        log_file.write(log_message + "\n")

@app.post("/send-log/")
async def send_log(background_tasks: BackgroundTasks, message: str):
    background_tasks.add_task(write_log, message)
    return {"message": "Log will be written in the background"}


# middleware
class SimpleMiddleWare(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        response = await call_next(request)
        response.headers["X-Custom-Header"] = "My Custom Header"
        return response
app.add_middleware(SimpleMiddleWare)


# CORS (Cross-Origin Resource Sharing) MiddleWare
app.add_middleware(
    CORSMiddleware,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)


# Authentication - OAuth2 Password Flow
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.get("/user/me/")
async def read_user_me(token: str = Depends(oauth2_scheme)):
    return {"token":token}


# WebSockets
async def websocket_endpoint(websocket : WebSocket):
    await websocket.accept()
    await websocket.send_text("Hello")
    await websocket.close()



'''
Eğer bir fonksiyonun başına async eklersek, fonksiyon asenkron hale gelir 
ve non-blocking olarak çalışır. Yani, fonksiyon çalışırken başka işler yapılabilir 
ve fonksiyonun tamamlanması beklenmez.

'''
