from sqlalchemy import Column, Integer, String
from app.database import Base

class Servico(Base):
    __tablename__ = "servicos"

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    preco_base = Column(Integer)