from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from decimal import Decimal

class PagamentoSchema(BaseModel):
    id_pagamento: Optional[int] = None
    id_corrida: int
    valor: Decimal
    id_metodo_pagamento: int
    datahora_transacao: datetime

    class Config:
        from_attributes = True