from pydantic import BaseModel
from datetime import datetime

class CorridaCreate(BaseModel):
    passageiro_id: int
    motorista_id: int
    servico_id: int
    classe_id: int
    origem: str
    destino: str

class CorridaOut(BaseModel):
    id: int
    passageiro_id: int
    motorista_id: int
    servico_id: int
    classe_id: int
    origem: str
    destino: str
    inicio: datetime | None
    fim: datetime | None

    class Config:
        from_attributes = True