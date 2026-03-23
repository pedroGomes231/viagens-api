from pydantic import BaseModel
from typing import Optional

class VeiculoSchema(BaseModel):
    id_veiculo: Optional[int] = None
    placa: str
    id_modelo: int
    tem_seguro: int
    id_classe: int

    class Config:
        from_attributes = True