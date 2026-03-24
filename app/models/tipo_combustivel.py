from sqlalchemy import Column, Integer, String, Numeric
from app.database import Base

class TipoCombustivel(Base):
    __tablename__ = "tipo_combustivel"

    id_combustivel = Column(Integer, primary_key=True, autoincrement=True)
    descricao = Column(String(45))
    fator_carbono = Column(Numeric(10, 5))