
from pydantic import BaseModel
from typing import Optional

class MetodoPagamentoSchema(BaseModel):
    id_metodo_pagamento: Optional[int] = None
    descricao: str
    nome_financeira: str

    class Config:
        from_attributes = True