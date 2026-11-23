from routers.router_faq import router_faq
from routers.router_auth import router_auth
from routers.router_ticket import router_ticket
from routers.router_category import router_category
from routers.router_message import router_message_ticket
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(router_auth)
app.include_router(router_ticket)
app.include_router(router_category)
app.include_router(router_message_ticket)
app.include_router(router_faq)