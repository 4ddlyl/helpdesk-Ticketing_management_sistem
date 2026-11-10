from routers.router_auth import router_auth
from routers.router_ticket import router_ticket
from fastapi import FastAPI

app = FastAPI()
app.include_router(router_auth)
app.include_router(router_ticket)