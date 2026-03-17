from sqlalchemy import Column, Integer, ForeignKey,String
from app.database import Base

class Pagamento(Base):
    __tablename__ = "pagamentos"

    id = Column(Integer, primary_key=True)

    corrida_id = Column(Integer, ForeignKey("corridas.id"))
    metodo_id = Column(Integer, ForeignKey("metodos_pagamento.id"))

    valor = Column(Integer)
    status = Column(String)