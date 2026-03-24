from sqlalchemy import Column, BigInteger, Numeric, ForeignKey
from app.database import Base

class Passageiro(Base):
    __tablename__ = "passageiro"

    id_passageiro = Column(BigInteger, primary_key=True, autoincrement=True)
    id_usuario = Column(BigInteger, ForeignKey("usuario.id_usuario"))
    media_avaliacao = Column(Numeric(3, 2))