from pydantic import BaseModel

class AvaliacaoCreate(BaseModel):
    corrida_id: int
    nota_motorista: int
    nota_passageiro: int

class AvaliacaoOut(BaseModel):
    id: int
    corrida_id: int
    nota_motorista: int
    nota_passageiro: int

    class Config:
        from_attributes = True