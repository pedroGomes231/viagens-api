from pydantic import BaseModel

class VeiculoCreate(BaseModel):
    placa: str
    cor: str
    ano: int
    modelo_id: int
    combustivel_id: int

class VeiculoOut(BaseModel):
    id: int
    placa: str
    cor: str
    ano: int
    modelo_id: int
    combustivel_id: int

    class Config:
        from_attributes = True