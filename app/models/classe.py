
from sqlalchemy import Column, Integer, String, Numeric
from app.database import Base

class Classe(Base):
    __tablename__ = "classe"

    id_classe = Column(Integer, primary_key=True, autoincrement=True)
    nome_classe = Column(String(45))
    fator_preco = Column(Numeric(10, 2))
    