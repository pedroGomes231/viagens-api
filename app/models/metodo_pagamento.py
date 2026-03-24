from sqlalchemy import Column, SmallInteger, String
from app.database import Base

class MetodoPagamento(Base):
    __tablename__ = "metodo_pagamentos"

    id_metodo_pagamento = Column(SmallInteger, primary_key=True, autoincrement=True)
    descricao = Column(String(45))
    nome_financeira = Column(String(45))

