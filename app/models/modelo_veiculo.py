
from sqlalchemy import Column, Integer, String, Enum, ForeignKey
from app.database import Base

class ModeloVeiculo(Base):
    __tablename__ = "modelo_veiculo"

    id_modelo = Column(Integer, primary_key=True, autoincrement=True)
    nome_modelo = Column(String(45))
    cor = Column(String(45))
    fabricante = Column(String(45))
    ano = Column(Integer)
    capacidade = Column(Integer)
    propriedade = Column(Enum("Próprio", "Alugado"))
    id_combustivel = Column(Integer, ForeignKey("tipo_combustivel.id_combustivel"))