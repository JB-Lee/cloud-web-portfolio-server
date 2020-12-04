from abc import ABCMeta, abstractmethod

from fastapi import FastAPI

from .event import PushEventManager
from .session import SessionManager


class RouteContainer(metaclass=ABCMeta):
    push_event_manager: PushEventManager
    session_manager: SessionManager
    app: FastAPI

    def attach(self, app: FastAPI, push_event_manager: PushEventManager, session_manager: SessionManager):
        self.app = app
        self.push_event_manager = push_event_manager
        self.session_manager = session_manager
        self.route()

    @abstractmethod
    def route(self):
        pass
