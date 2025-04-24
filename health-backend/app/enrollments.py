from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from . import crud, database

router = APIRouter(prefix="/enrollments", tags=["Enrollments"])

# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

class EnrollmentRequest(BaseModel):
    client_id: int
    program_ids: list[int]

@router.post("/")
def enroll_client(enrollment: EnrollmentRequest, db: Session = Depends(get_db)):
    try:
        client = crud.enroll_client(db, enrollment.client_id, enrollment.program_ids)
        return {"message": "Client successfully enrolled", "client": client.id}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
