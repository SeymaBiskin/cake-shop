from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import cakes, root

app = FastAPI()


app.include_router(
    root.router,
    tags=["root"],
)

app.include_router(
    cakes.router,
    tags=["cake"],
)


origins = [
    "http://localhost:3000",
    "http://localhost:8000",
    "http://127.0.0.1:3000",
    "http://127.0.0.1:8000",
    "http://web:8000",
    "http://localhost",
    "http://0.0.0.0",
    "*"      
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


