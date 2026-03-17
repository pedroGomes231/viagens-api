from pydantic import BaseModel

class UsuarioCreate(BaseModel):
    nome: str
    email: str
    cpf: str

class UsuarioOut(BaseModel):
    id: int
    nome: str
    email: str
    cpf: str

    class Config:
        from_attributes = True