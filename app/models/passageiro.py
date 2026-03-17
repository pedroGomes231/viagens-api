from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Passageiro(Base):
    __tablename__ = "passageiros"

    id = Column(Integer, ForeignKey("usuarios.id"), primary_key=True)

    usuario = relationship("Usuario")