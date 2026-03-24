
from sqlalchemy import Column, Integer, CHAR, ForeignKey
from app.database import Base

class Veiculo(Base):
    __tablename__ = "veiculo"

    id_veiculo = Column(Integer, primary_key=True, autoincrement=True)
    placa = Column(CHAR(7))
    id_modelo = Column(Integer, ForeignKey("modelo_veiculo.id_modelo"))
    tem_seguro = Column(Integer)
    id_classe = Column(Integer, ForeignKey("classe.id_classe"))