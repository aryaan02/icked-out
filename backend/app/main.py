from fastapi import FastAPI
from app.routers import icks, users, comments
from app.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(icks.router, prefix="/api", tags=["Icks"])
app.include_router(users.router, prefix="/api", tags=["Users"])
app.include_router(comments.router, prefix="/api", tags=["Comments"])
