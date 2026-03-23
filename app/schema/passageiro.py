from pydantic import BaseModel
from typing import Optional
from decimal import Decimal

class PassageiroSchema(BaseModel):
    id_passageiro: Optional[int] = None
    id_usuario: int
    media_avaliacao: Optional[Decimal] = None

    class Config:
        from_attributes = True