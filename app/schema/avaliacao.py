from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class AvaliacaoSchema(BaseModel):
   
    nota_passageiro: Optional[int] = None
    nota_motorista: Optional[int] = None
    datahora_limite: datetime

    class Config:
        from_attributes = True