from pydantic import BaseModel

class TipoCombustivelCreate(BaseModel):
    nome: str

class TipoCombustivelOut(BaseModel):
    id: int
    nome: str

    class Config:
        from_attributes = True