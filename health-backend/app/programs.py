from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from . import crud, schemas, database

router = APIRouter(prefix="/programs", tags=["Programs"])

# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.Program)
def create_program(program: schemas.ProgramCreate, db: Session = Depends(get_db)):
    return crud.create_program(db, program)

@router.get("/", response_model=list[schemas.Program])
def list_programs(db: Session = Depends(get_db)):
    return db.query(crud.models.Program).all()
