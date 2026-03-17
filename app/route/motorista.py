from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.motorista import Motorista
from app.schema.motorista import MotoristaCreate, MotoristaOut

router = APIRouter(prefix="/motorista",tags=["Motorista"])


@router.post("/", response_model=MotoristaOut)
def criar(dados: MotoristaCreate, db: Session = Depends(get_db)):
    novo = Motorista(**dados.model_dump())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

#Listar todas as classes
@router.get("/", response_model=list[MotoristaOut])
def listar(db: Session = Depends(get_db)):
    return db.query(Motorista).all()

#Buscar por id da classe
@router.get("/{id}", response_model=MotoristaOut)
def buscar(id: int, db: Session = Depends(get_db)):
    novo = db.query(Motorista).get(id)
    if not novo:
        raise HTTPException(status_code=404, detail="Motorista não encontrado")
    return novo


@router.put("/{id}", response_model=MotoristaOut)
def atualizar(id: int, dados: MotoristaCreate, db: Session = Depends(get_db)):
    novo = db.query(Motorista).get(id)
    if not novo:
        raise HTTPException(status_code=404, detail="Motorista não encontrado")

    for campo, valor in dados.model_dump().items():
        setattr(novo, campo, valor)

    db.commit()
    db.refresh(novo)
    return novo

#Deletar a classe
@router.delete("/{id}")
def deletar(id: int, db: Session = Depends(get_db)):
    novo = db.query(Motorista).get(id)
    if not novo:
        raise HTTPException(status_code=404, detail="Motorista não encontrado")

    db.delete(novo)
    db.commit()
    return {"ok": True}