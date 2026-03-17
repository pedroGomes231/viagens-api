from pydantic import BaseModel

class ServicoCreate(BaseModel):
    nome: str
    preco_base: int

class ServicoOut(BaseModel):
    id: int
    nome: str
    preco_base: int

    class Config:
        from_attributes = True