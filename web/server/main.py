import os, asyncio, json
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import FileResponse
import websockets

app = FastAPI()
ROVER_IP = os.getenv("ROVER_IP", "192.168.1.50")
ROVER_WS_PORT = int(os.getenv("ROVER_WS_PORT", "8765"))

@app.get("/")
async def index():
    return FileResponse("static/index.html")

@app.websocket("/ws")
async def ws(ws: WebSocket):
    await ws.accept()
    try:
        async with websockets.connect(f"ws://{ROVER_IP}:{ROVER_WS_PORT}") as rover:
            async def to_rover():
                while True:
                    msg = await ws.receive_text()
                    await rover.send(msg)
            async def to_client():
                while True:
                    msg = await rover.recv()
                    await ws.send_text(msg)
            await asyncio.gather(to_rover(), to_client())
    except WebSocketDisconnect:
        pass
    except Exception as e:
        await ws.send_text(json.dumps({"type":"error","message":str(e)}))
