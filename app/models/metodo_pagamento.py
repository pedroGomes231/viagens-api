from sqlalchemy import Column, Integer, String
from app.database import Base

class MetodoPagamento(Base):
    __tablename__ = "metodos_pagamento"

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)