from pydantic import BaseModel
from typing import List, Optional

class ProgramBase(BaseModel):
    title: str
    description: str

class ProgramCreate(ProgramBase):
    pass

class Program(ProgramBase):
    id: int
    class Config:
        orm_mode = True

class ClientBase(BaseModel):
    name: str
    email: str

class ClientCreate(ClientBase):
    pass

class Client(ClientBase):
    id: int
    programs: List[Program] = []
    class Config:
        orm_mode = True
