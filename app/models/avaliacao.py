from sqlalchemy import Column, Integer, ForeignKey
from app.database import Base

class Avaliacao(Base):
    __tablename__ = "avaliacoes"

    id = Column(Integer, primary_key=True)
    corrida_id = Column(Integer, ForeignKey("corridas.id"))

    nota_motorista = Column(Integer)
    nota_passageiro = Column(Integer)