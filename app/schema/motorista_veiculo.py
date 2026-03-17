from pydantic import BaseModel

class MotoristaVeiculoCreate(BaseModel):
    motorista_id: int
    veiculo_id: int

class MotoristaVeiculoOut(BaseModel):
    motorista_id: int
    veiculo_id: int

    class Config:
        from_attributes = True