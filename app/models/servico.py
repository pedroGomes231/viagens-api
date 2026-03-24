
from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base

class Servico(Base):
    __tablename__ = "servico"

    id_servico = Column(Integer, primary_key=True, autoincrement=True)
    nome_servico = Column(String(50))
    id_classe_minima = Column(Integer, ForeignKey("classe.id_classe"))