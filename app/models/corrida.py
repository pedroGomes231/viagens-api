from sqlalchemy import Column, BigInteger, Integer, DateTime, String, Numeric, Enum, ForeignKey
from app.database import Base

class Corrida(Base):
    __tablename__ = "corrida"

    id_corrida = Column(BigInteger, primary_key=True, autoincrement=True)
    id_passageiro = Column(BigInteger, ForeignKey("passageiro.id_passageiro"))
    id_motorista = Column(BigInteger, ForeignKey("motorista.id_motorista"))
    id_servico = Column(Integer, ForeignKey("servico.id_servico"))
    id_avaliacao = Column(BigInteger, ForeignKey("avaliacao.id_avaliacao"))
    datahora_inicio = Column(DateTime)
    datahora_fim = Column(DateTime)
    local_partida = Column(String(50))
    local_destino = Column(String(50))
    valor_estimado = Column(Numeric(10, 2))
    status = Column(Enum("Pendente", "Em andamento", "Concluída", "Cancelada"))

