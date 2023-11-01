from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import cakes

app = FastAPI()


app.include_router(
    cakes.router,
    tags=["cake"],
)


origins = [
    "*"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)