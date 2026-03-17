from pydantic import BaseModel

class MetodoPagamentoCreate(BaseModel):
    nome: str

class MetodoPagamentoOut(BaseModel):
    id: int
    nome: str

    class Config:
        from_attributes = True