from fastapi import FastAPI

from app.api.routes import router
from app.api.v1.routes import router_v1

app = FastAPI()

app.include_router(router)
app.include_router(router_v1)