from routers.router_auth import router_auth
from routers.router_ticket import router_ticket
from routers.router_category import router_category
from fastapi import FastAPI

app = FastAPI()
app.include_router(router_auth)
app.include_router(router_ticket)
app.include_router(router_category)