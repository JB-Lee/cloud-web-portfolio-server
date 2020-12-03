from apscheduler.schedulers.asyncio import AsyncIOScheduler
from fastapi import FastAPI

from .route.auth import AuthRoute
from .route.test import DefaultRoute
from .schedule.crawler import CrawlingJob
from .scheduler import Scheduler

App = FastAPI()

scheduler = Scheduler(AsyncIOScheduler())

DefaultRoute().attach(App, scheduler)
AuthRoute().attach(App, scheduler)

scheduler.register_job(CrawlingJob())
scheduler.start()
