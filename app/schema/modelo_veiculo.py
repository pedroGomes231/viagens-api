from pydantic import BaseModel
from typing import Optional

class ModeloVeiculoSchema(BaseModel):
    id_modelo: Optional[int] = None
    nome_modelo: str
    cor: str
    fabricante: str
    ano: int
    capacidade: int
    propriedade: str
    id_combustivel: int

    class Config:
        from_attributes = True