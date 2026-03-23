from pydantic import BaseModel
from decimal import Decimal

class ClasseSchema(BaseModel):
    
    nome_classe: str
    fator_preco: Decimal

    class Config:
        from_attributes = True