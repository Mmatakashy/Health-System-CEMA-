from fastapi import FastAPI
from app import clients, programs, enrollments
from app.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(clients.router)
app.include_router(programs.router)
app.include_router(enrollments.router)
