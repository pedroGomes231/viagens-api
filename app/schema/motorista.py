from pydantic import BaseModel

class MotoristaCreate(BaseModel):
    id: int
    cnh: str
    nome: str

class MotoristaOut(BaseModel):
    id: int
    cnh: str
    nome: str

    class Config:
        from_attributes = True