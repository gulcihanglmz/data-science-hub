# main.py
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from typing import List
import json
from datetime import datetime

app = FastAPI()

class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []
        self.connection_count = 0

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)
        self.connection_count += 1
        print(f"New connection established. Total connections: {self.connection_count}")

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)
        self.connection_count -= 1
        print(f"Connection closed. Total connections: {self.connection_count}")

    async def broadcast(self, message: str):
        print(f"Broadcasting message: {message}")
        for connection in self.active_connections:
            await connection.send_text(message)

manager = ConnectionManager()

@app.get("/")
async def get():
    return {"message": "WebSocket Server is running"}

@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: str):
    await manager.connect(websocket)
    print(f"Client {client_id} connected")

    try:
        while True:
            data = await websocket.receive_text()

            try:
                message_data = json.loads(data)
                timestamp = datetime.now().strftime("%H:%M:%S")
                message_data.update({
                    "client_id": client_id,
                    "timestamp": timestamp
                })
                print(f"Received from client {client_id}: {message_data['message']}")
                await manager.broadcast(json.dumps(message_data))

            except json.JSONDecodeError:
                print(f"Received plain text from client {client_id}: {data}")
                await manager.broadcast(f"Client {client_id}: {data}")

    except WebSocketDisconnect:
        manager.disconnect(websocket)
        disconnect_message = f"Client #{client_id} left the chat"
        print(disconnect_message)
        await manager.broadcast(json.dumps({
            "client_id": "system",
            "message": disconnect_message,
            "timestamp": datetime.now().strftime("%H:%M:%S"),
            "type": "disconnect"
        }))

'''
Bir istemci, sunucuya bir mesaj gönderdi.
Sunucu, bu mesajı aldı ve diğer istemcilere iletti.
'''
