from pydantic import BaseModel

class PassageiroCreate(BaseModel):
    id: int
    nome: str

class PassageiroOut(BaseModel):
    id: int
    nome: str

    class Config:
        from_attributes = True