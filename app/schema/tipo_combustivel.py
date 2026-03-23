from pydantic import BaseModel
from decimal import Decimal

class TipoCombustivelSchema(BaseModel):
    descricao: str
    fator_carbono: Decimal

    class Config:
        from_attributes = True