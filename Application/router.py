from abc import ABCMeta, abstractmethod

from fastapi import FastAPI

from .scheduler import Scheduler


class RouteContainer(metaclass=ABCMeta):
    scheduler: Scheduler
    app: FastAPI

    def attach(self, app: FastAPI, scheduler: Scheduler):
        self.app = app
        self.scheduler = scheduler
        self.route()

    @abstractmethod
    def route(self):
        pass
