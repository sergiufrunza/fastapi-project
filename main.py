from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import asyncio
import logging
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []
        self.lock = asyncio.Lock()

    async def connect(self, websocket: WebSocket):
        async with self.lock:
            await websocket.accept()
            self.active_connections.append(websocket)
            logging.info(f"New connection: {websocket.client}")

    async def disconnect(self, websocket: WebSocket):
        async with self.lock:
            if websocket in self.active_connections:
                self.active_connections.remove(websocket)
                logging.info(f"Disconnected: {websocket.client}")

    async def broadcast(self, message: dict):
        disconnected_clients = []
        async with self.lock:
            for connection in self.active_connections:
                try:
                    await connection.send_json(message)
                except Exception as e:
                    logging.error(f"Error sending message: {e}")
                    disconnected_clients.append(connection)
            for client in disconnected_clients:
                self.active_connections.remove(client)


manager = ConnectionManager()


@app.websocket("/ws/chat")
async def websocket_chat(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_json()
            role = data.get("role", "")
            message = data.get("message", "")

            response = {
                "role": role,
                "message": message
            }
            await manager.broadcast(response)
    except WebSocketDisconnect:
        manager.disconnect(websocket)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)