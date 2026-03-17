from sqlalchemy import Column, Integer, ForeignKey
from app.database import Base

class MotoristaVeiculo(Base):
    __tablename__ = "motorista_veiculo"

    motorista_id = Column(Integer, ForeignKey("motoristas.id"), primary_key=True)
    veiculo_id = Column(Integer, ForeignKey("veiculos.id"), primary_key=True)