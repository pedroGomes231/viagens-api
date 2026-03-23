from sqlalchemy import VARCHAR, Column, Integer, Text, String, CHAR, Date, SmallInteger
from app.database import Base

class Usuario(Base):
    __tablename__ = "usuario"

    id_usuario = Column(Integer, primary_key=True)
    nome = Column(Text)
    cpf = Column(CHAR(11), unique=True)
    data_nascimento = Column(Date)
    idade = Column(SmallInteger)
    senha = Column(CHAR(64))
    email = Column(VARCHAR(255), unique=True)
    usuario = Column(String(50), unique=True)