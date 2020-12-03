from fastapi import WebSocket, WebSocketDisconnect

from ..router import RouteContainer


class DefaultRoute(RouteContainer):
    def route(self):
        @self.app.get("/test/testing")
        async def test():
            return {"result": "asd"}

        @self.app.websocket("/ws/add_watcher/{event}")
        async def websocket_endpoint(websocket: WebSocket, event: str):
            await websocket.accept()
            await self.push_event_manager.add_watcher(event, websocket)
            try:
                await websocket.receive()
                self.push_event_manager.remove_watcher(event, websocket)

            except WebSocketDisconnect:
                print(event + " disconnect")
                self.push_event_manager.remove_watcher(event, websocket)
