from pydantic import BaseModel

class ClasseCreate(BaseModel):
    nome: str

class ClasseOut(BaseModel):
    id: int
    nome: str

    class Config:
        from_attributes = True