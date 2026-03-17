from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from app.database import Base

class Corrida(Base):
    __tablename__ = "corridas"

    id = Column(Integer, primary_key=True)

    passageiro_id = Column(Integer, ForeignKey("passageiros.id"))
    motorista_id = Column(Integer, ForeignKey("motoristas.id"))
    servico_id = Column(Integer, ForeignKey("servicos.id"))
    classe_id = Column(Integer, ForeignKey("classes.id"))

    origem = Column(String, nullable=False)
    destino = Column(String, nullable=False)
    inicio = Column(DateTime)
    fim = Column(DateTime)