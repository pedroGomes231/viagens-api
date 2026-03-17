from sqlalchemy import Column, Integer, String
from app.database import Base

class TipoCombustivel(Base):
    __tablename__ = "tipo_combustivel"

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)