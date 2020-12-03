import asyncio
from typing import Any, Dict


class Listener:
    watchers: Dict

    def __init__(self):
        self.watchers = dict()

    async def invoke(self, event: Any, *args, **kwargs):
        watcher = self.watchers.get(event)
        if watcher:
            for future in watcher:
                future.set_result({"event": event, "args": args, "kwargs": kwargs})

            watcher.clear()

    async def add_watcher(self, event) -> asyncio.Future:
        loop = asyncio.get_running_loop()
        future = loop.create_future()

        if event not in self.watchers:
            self.watchers[event] = list()

        self.watchers[event].append(future)

        return future
