from pydantic import BaseModel
from typing import Optional
from datetime import date

class UsuarioSchema(BaseModel):
    id_usuario: Optional[int] = None
    nome: str
    email: str
    cpf: str
    senha: str
    data_nascimento: date
    idade: int
    usuario: str

    class Config:
        from_attributes = True