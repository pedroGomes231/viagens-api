from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Motorista(Base):
    __tablename__ = "motoristas"

    id = Column(Integer, ForeignKey("usuarios.id"), primary_key=True)
    cnh = Column(String, unique=True, nullable=False)
    nome = Column(String, nullable=False)

    usuario = relationship("Usuario")