from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.servico import Servico
from app.schema.servico import ServicoCreate, ServicoOut

router = APIRouter(prefix="/servico",tags=["Servico"])


@router.post("/", response_model=ServicoOut)
def criar(dados: ServicoCreate, db: Session = Depends(get_db)):
    novo = Servico(**dados.model_dump())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

#Listar todas as classes
@router.get("/", response_model=list[ServicoOut])
def listar(db: Session = Depends(get_db)):
    return db.query(Servico).all()

#Buscar por id da classe
@router.get("/{id}", response_model=ServicoOut)
def buscar(id: int, db: Session = Depends(get_db)):
    novo = db.query(Servico).get(id)
    if not novo:
        raise HTTPException(status_code=404, detail="Servico não encontrado")
    return novo


@router.put("/{id}", response_model=ServicoOut)
def atualizar(id: int, dados: ServicoCreate, db: Session = Depends(get_db)):
    novo = db.query(Servico).get(id)
    if not novo:
        raise HTTPException(status_code=404, detail="Servico não encontrado")

    for campo, valor in dados.model_dump().items():
        setattr(novo, campo, valor)

    db.commit()
    db.refresh(novo)
    return novo

#Deletar a classe
@router.delete("/{id}")
def deletar(id: int, db: Session = Depends(get_db)):
    novo = db.query(Servico).get(id)
    if not novo:
        raise HTTPException(status_code=404, detail="Servico não encontrado")

    db.delete(novo)
    db.commit()
    return {"ok": True}