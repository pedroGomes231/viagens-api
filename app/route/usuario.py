from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import usuario
from app.models.usuario import Usuario
from app.schema.usuario import UsuarioCreate, UsuarioOut

router = APIRouter(prefix="/Usuario",tags=["Usuario"])


@router.post("/", response_model=UsuarioOut)
def criar(dados: UsuarioCreate, db: Session = Depends(get_db)):
    novo = Usuario(**dados.model_dump())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

#Listar todas as classes
@router.get("/", response_model=list[UsuarioOut])
def listar(db: Session = Depends(get_db)):
    return db.query(Usuario).all()

#Buscar por id da classe
@router.get("/{id}", response_model=UsuarioOut)
def buscar(id: int, db: Session = Depends(get_db)):
    novo = db.query(Usuario).get(id)
    if not novo:
        raise HTTPException(status_code=404, detail="Usuario não encontrada")
    return novo


@router.put("/{id}", response_model=UsuarioOut)
def atualizar(id: int, dados: UsuarioCreate, db: Session = Depends(get_db)):
    novo = db.query(usuario).get(id)
    if not novo:
        raise HTTPException(status_code=404, detail="Usuario não encontrada")

    for campo, valor in dados.dict().items():
        setattr(novo, campo, valor)

    db.commit()
    db.refresh(novo)
    return novo

#Deletar a classe
@router.delete("/{id}")
def deletar(id: int, db: Session = Depends(get_db)):
    novo = db.query(Usuario).get(id)
    if not novo:
        raise HTTPException(status_code=404, detail="Usuario")

    db.delete(novo)
    db.commit()
    return {"ok": True}