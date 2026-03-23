from pydantic import BaseModel
from typing import Optional
from decimal import Decimal

class MotoristaSchema(BaseModel):
    id_motorista: Optional[int] = None
    id_usuario: int
    media_avaliacao: Optional[Decimal] = None
    cnh: int

    class Config:
        from_attributes = True