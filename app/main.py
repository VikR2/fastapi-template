from fastapi.middleware.cors import CORSMiddleware

from typing import Optional, List
from importlib_metadata import Deprecated
from fastapi import Body, FastAPI, Depends
from . import models
from .database import engine, get_db
from .routers import post, users, auth, vote
from .config import settings





#sqlaclhemy initial creation
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#from post import APIRouter via router
app.include_router(post.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(vote.router)