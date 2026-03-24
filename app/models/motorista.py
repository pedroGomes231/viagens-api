from sqlalchemy import Column, BigInteger, Numeric, ForeignKey
from app.database import Base

class Motorista(Base):
    __tablename__ = "motorista"

    id_motorista = Column(BigInteger, primary_key=True, autoincrement=True)
    id_usuario = Column(BigInteger, ForeignKey("usuario.id_usuario"))
    media_avaliacao = Column(Numeric(3, 2))
    cnh = Column(BigInteger)