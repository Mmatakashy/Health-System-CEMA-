from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from ..database import Base

enrollments_table = Table(
    'enrollments', Base.metadata,
    Column('client_id', ForeignKey('clients.id'), primary_key=True),
    Column('program_id', ForeignKey('programs.id'), primary_key=True)
)

class Client(Base):
    __tablename__ = "clients"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)
    programs = relationship("Program", secondary=enrollments_table, back_populates="clients")

class Program(Base):
    __tablename__ = "programs"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    clients = relationship("Client", secondary=enrollments_table, back_populates="programs")
