from abc import ABCMeta, abstractmethod

from fastapi import FastAPI

from .event import PushEventManager


class RouteContainer(metaclass=ABCMeta):
    push_event_manager: PushEventManager
    app: FastAPI

    def attach(self, app: FastAPI, push_event_manager: PushEventManager):
        self.app = app
        self.push_event_manager = push_event_manager
        self.route()

    @abstractmethod
    def route(self):
        pass
