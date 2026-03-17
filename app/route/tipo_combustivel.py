from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.tipo_combustivel import TipoCombustivel
from app.schema.tipo_combustivel import TipoCombustivelCreate, TipoCombustivelOut

router = APIRouter(prefix="/tipo_combustivel",tags=["Tipo Combustivel"])


@router.post("/", response_model=TipoCombustivelOut)
def criar(dados: TipoCombustivelCreate, db: Session = Depends(get_db)):
    novo = TipoCombustivel(**dados.model_dump())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

#Listar todas as classes
@router.get("/", response_model=list[TipoCombustivelOut])
def listar(db: Session = Depends(get_db)):
    return db.query(TipoCombustivel).all()

#Buscar por id da classe
@router.get("/{id}", response_model=TipoCombustivelOut)
def buscar(id: int, db: Session = Depends(get_db)):
    novo = db.query(TipoCombustivel).get(id)
    if not novo:
        raise HTTPException(status_code=404, detail="Nenhum tipo de combustivel")
    return novo


@router.put("/{id}", response_model=TipoCombustivelOut)
def atualizar(id: int, dados: TipoCombustivelCreate, db: Session = Depends(get_db)):
    novo = db.query(TipoCombustivel).get(id)
    if not novo:
        raise HTTPException(status_code=404, detail="Nenhum tipo de combustivel")

    for campo, valor in dados.model_dump().items():
        setattr(novo, campo, valor)

    db.commit()
    db.refresh(novo)
    return novo

#Deletar a classe
@router.delete("/{id}")
def deletar(id: int, db: Session = Depends(get_db)):
    novo = db.query(TipoCombustivel).get(id)
    if not novo:
        raise HTTPException(status_code=404, detail="Nenhim tipo de cimbustivel")

    db.delete(novo)
    db.commit()
    return {"ok": True}