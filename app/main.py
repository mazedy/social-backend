from fastapi import FastAPI
from .routes import router
from . import config  # ensures Neo4j connection loads

app = FastAPI(title="Social Media Backend with Neo4j + FastAPI")

app.include_router(router)
