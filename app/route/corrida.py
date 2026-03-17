from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.corrida import Corrida
from app.schema.corrida import CorridaCreate, CorridaOut

router = APIRouter(prefix="/corrida",tags=["corrida"])


@router.post("/", response_model=CorridaOut)
def criar(dados: CorridaCreate, db: Session = Depends(get_db)):
    novo = Corrida(**dados.model_dump())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

#Listar todas as classes
@router.get("/", response_model=list[CorridaOut])
def listar(db: Session = Depends(get_db)):
    return db.query(Corrida).all()

#Buscar por id da classe
@router.get("/{id}", response_model=CorridaOut)
def buscar(id: int, db: Session = Depends(get_db)):
    novo = db.query(Corrida).get(id)
    if not novo:
        raise HTTPException(status_code=404, detail="COrrida não encontrada")
    return novo


@router.put("/{id}", response_model=CorridaOut)
def atualizar(id: int, dados: CorridaCreate, db: Session = Depends(get_db)):
    novo = db.query(Corrida).get(id)
    if not novo:
        raise HTTPException(status_code=404, detail="Corrida não encontrada")

    for campo, valor in dados.model_dump().items():
        setattr(novo, campo, valor)

    db.commit()
    db.refresh(novo)
    return novo

#Deletar a classe
@router.delete("/{id}")
def deletar(id: int, db: Session = Depends(get_db)):
    novo = db.query(Corrida).get(id)
    if not novo:
        raise HTTPException(status_code=404, detail="Corrida não encontrada")

    db.delete(novo)
    db.commit()
    return {"ok": True}