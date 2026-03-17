from pydantic import BaseModel

class ModeloVeiculoCreate(BaseModel):
    nome: str

class ModeloVeiculoOut(BaseModel):
    id: int
    nome: str

    class Config:
        from_attributes = True