from sqlalchemy import Column, Integer, String
from app.database import Base

class ModeloVeiculo(Base):
    __tablename__ = "modelo_veiculo"

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)