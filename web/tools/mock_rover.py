import asyncio, websockets, json
async def handler(ws):
    async for msg in ws:
        print("reçu:", msg)
        await ws.send(json.dumps({"type":"ack","received":msg}))
async def main():
    async with websockets.serve(handler, "0.0.0.0", 8765):
        await asyncio.Future()
asyncio.run(main())
