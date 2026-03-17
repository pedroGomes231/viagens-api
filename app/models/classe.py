from sqlalchemy import Column, Integer, String
from app.database import Base

class Classe(Base):
    __tablename__ = "classes"

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)