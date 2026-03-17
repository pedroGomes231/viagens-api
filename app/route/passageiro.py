from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import passageiro
from app.models.passageiro import Passageiro
from app.schema.passageiro import PassageiroCreate, PassageiroOut

router = APIRouter(prefix="/passageiro",tags=["Passageiro"])


@router.post("/", response_model=PassageiroOut)
def criar(dados: PassageiroCreate, db: Session = Depends(get_db)):
    novo = Passageiro(**dados.model_dump())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

#Listar todas as classes
@router.get("/", response_model=list[PassageiroOut])
def listar(db: Session = Depends(get_db)):
    return db.query(Passageiro).all()

#Buscar por id da classe
@router.get("/{id}", response_model=PassageiroOut)
def buscar(id: int, db: Session = Depends(get_db)):
    novo = db.query(Passageiro).get(id)
    if not novo:
        raise HTTPException(status_code=404, detail="Nenhum Passageiro encontrado")
    return novo


@router.put("/{id}", response_model=PassageiroOut)
def atualizar(id: int, dados: PassageiroCreate, db: Session = Depends(get_db)):
    novo = db.query(passageiro).get(id)
    if not novo:
        raise HTTPException(status_code=404, detail="Nenhum Passageiro não encontrado")

    for campo, valor in dados.model_dump().items():
        setattr(novo, campo, valor)

    db.commit()
    db.refresh(novo)
    return novo

#Deletar a classe
@router.delete("/{id}")
def deletar(id: int, db: Session = Depends(get_db)):
    obj = db.query(Passageiro).get(id)
    if not obj:
        raise HTTPException(status_code=404, detail="Nenhum Passageiro não encontrado")

    db.delete(obj)
    db.commit()
    return {"ok": True}