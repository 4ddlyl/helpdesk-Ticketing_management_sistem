from routers.router_auth import router_auth
from fastapi import FastAPI

app = FastAPI()
app.include_router(router_auth)