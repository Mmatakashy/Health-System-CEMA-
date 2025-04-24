from sqlalchemy.orm import Session
from .. import models, schemas

def create_client(db: Session, client: schemas.ClientCreate):
    db_client = models.Client(**client.dict())
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client

def create_program(db: Session, program: schemas.ProgramCreate):
    db_program = models.Program(**program.dict())
    db.add(db_program)
    db.commit()
    db.refresh(db_program)
    return db_program

def enroll_client(db: Session, client_id: int, program_ids: list):
    client = db.query(models.Client).filter(models.Client.id == client_id).first()
    programs = db.query(models.Program).filter(models.Program.id.in_(program_ids)).all()
    client.programs.extend(programs)
    db.commit()
    return client
# Update client
def update_client(db: Session, client_id: int, client_data: schemas.ClientCreate):
    client = db.query(models.Client).filter(models.Client.id == client_id).first()
    if client:
        for key, value in client_data.dict().items():
            setattr(client, key, value)
        db.commit()
        db.refresh(client)
    return client

# Delete client
def delete_client(db: Session, client_id: int):
    client = db.query(models.Client).filter(models.Client.id == client_id).first()
    if client:
        db.delete(client)
        db.commit()
    return client

