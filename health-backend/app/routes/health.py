from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.models import Patient
from app.schemas import PatientCreate
from app.crud import create_patient
from app.database import engine

router = APIRouter(prefix="/patients", tags=["Patients"])

def get_session():
    with Session(engine) as session:
        yield session

@router.post("/")
def add_patient(data: PatientCreate, session: Session = Depends(get_session)):
    patient = Patient(**data.dict())
    return create_patient(session, patient)
