from fastapi import WebSocket

from ..router import RouteContainer


class DefaultRoute(RouteContainer):
    def route(self):
        @self.app.get("/test/testing")
        async def test():
            return {"result": "asd"}

        @self.app.get("/test/polling")
        async def test_polling():
            res = await self.scheduler.add_watcher("test")
            return res

        @self.app.websocket("/ws")
        async def websocket_endpoint(websocket: WebSocket):
            await websocket.accept()
            while True:
                data = await websocket.receive()
                await websocket.send_text(f"Message text was: {data}")
