from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class MotoristaVeiculoSchema(BaseModel):
    id_motorista: int
    id_veiculo: int
    datahora_inicio: datetime
    datahora_fim: Optional[datetime] = None

    class Config:
        from_attributes = True