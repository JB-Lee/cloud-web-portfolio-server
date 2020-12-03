from __future__ import annotations

from abc import ABCMeta, abstractmethod
from typing import List, Dict

from apscheduler.schedulers.base import BaseScheduler

from .listener import Listener


class JobContainer(metaclass=ABCMeta):
    listener: Listener
    scheduler: BaseScheduler

    def attach(self, listener: Listener, scheduler: BaseScheduler):
        self.listener = listener
        self.scheduler = scheduler
        self.jobs()

    @abstractmethod
    def jobs(self):
        pass


class Scheduler:
    scheduler: BaseScheduler
    listener: Listener
    jobs: List[JobContainer]

    def __init__(self, scheduler):
        self.scheduler = scheduler
        self.listener = Listener()
        self.jobs = list()

    def register_job(self, job: JobContainer):
        job.attach(scheduler=self.scheduler, listener=self.listener)
        self.jobs.append(job)

    def start(self):
        self.scheduler.start()

    async def add_watcher(self, event) -> Dict:
        return await (await self.listener.add_watcher(event))
