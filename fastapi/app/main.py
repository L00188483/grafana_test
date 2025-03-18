import logging
import random

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
# from prometheus_client import Counter, Gauge
from prometheus_fastapi_instrumentator import Instrumentator


logger = logging.getLogger("uvicorn")
logger.setLevel(logging.INFO)


f_app = FastAPI()


# enable metrics for Prometheus
instrumentator = Instrumentator().instrument(f_app).expose(f_app)




class HelloResponseModel(BaseModel):
    hello: str


@f_app.get("/hello/{name}")
def hello(name: str) -> HelloResponseModel:
    return HelloResponseModel(hello=name)
