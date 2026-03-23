from sqlalchemy import Column, Integer, ForeignKey,DateTime
from app.database import Base

class Avaliacao(Base):
    __tablename__ = "avaliacoes"

    id = Column(Integer, primary_key=True)
    corrida_id = Column(Integer, ForeignKey("corridas.id"))
    datahora_limite = Column(DateTime)
    nota_motorista = Column(Integer)
    nota_passageiro = Column(Integer)