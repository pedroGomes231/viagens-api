from pydantic import BaseModel

class PagamentoCreate(BaseModel):
    corrida_id: int
    metodo_id: int
    valor: int
    status: str

class PagamentoOut(BaseModel):
    id: int
    corrida_id: int
    metodo_id: int
    valor: int
    status: str

    class Config:
        from_attributes = True