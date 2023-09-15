from fastapi import FastAPI, WebSocket, WebSocketDisconnect

app = FastAPI()

class WebSocketClient:
    def __init__(self, websocket: WebSocket):
        self.websocket = websocket

clients = {}

@app.websocket("/chat")
async def chat_endpoint(websocket: WebSocket):
    await websocket.accept()
    client_id = id(websocket)
    clients[client_id] = WebSocketClient(websocket)

    try:
        while True:
            message = await websocket.receive_text()
            response = f"Your question: {message}"
            await websocket.send_text(response)
    except WebSocketDisconnect:
        del clients[client_id]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)