from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Veiculo(Base):
    __tablename__ = "veiculos"

    id = Column(Integer, primary_key=True)
    placa = Column(String, unique=True, nullable=False)
    cor = Column(String)
    ano = Column(Integer)

    modelo_id = Column(Integer, ForeignKey("modelo_veiculo.id"))
    combustivel_id = Column(Integer, ForeignKey("tipo_combustivel.id"))

    modelo = relationship("ModeloVeiculo")
    combustivel = relationship("TipoCombustivel")