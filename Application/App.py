from apscheduler.schedulers.asyncio import AsyncIOScheduler
from fastapi import FastAPI

from .event import PushEventManager
from .route.auth import AuthRoute
from .route.test import DefaultRoute
from .schedule.crawler import CrawlingJob
from .scheduler import Scheduler

App = FastAPI()

pem = PushEventManager()
scheduler = Scheduler(AsyncIOScheduler(), pem)

DefaultRoute().attach(App, pem)
AuthRoute().attach(App, pem)

scheduler.register_job(CrawlingJob())
scheduler.start()
