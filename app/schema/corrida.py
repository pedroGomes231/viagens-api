from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from decimal import Decimal

class CorridaSchema(BaseModel):
    
    id_passageiro: int
    id_motorista: int
    id_servico: int
    id_avaliacao: Optional[int] = None
    datahora_inicio: datetime
    datahora_fim: Optional[datetime] = None
    local_partida: str
    local_destino: str
    valor_estimado: Decimal
    status: str

    class Config:
        from_attributes = True