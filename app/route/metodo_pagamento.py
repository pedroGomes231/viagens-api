from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import metodo_pagamento
from app.models.metodo_pagamento import MetodoPagamento
from app.schema.metodo_pagamento import MetodoPagamentoCreate, MetodoPagamentoOut

router = APIRouter(prefix="/metodo_pagamento",tags=["metodo pagamento"])


@router.post("/", response_model=MetodoPagamentoOut)
def criar(dados: MetodoPagamentoCreate, db: Session = Depends(get_db)):
    novo = MetodoPagamento (**dados.model_dump())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

#Listar todas as classes
@router.get("/", response_model=list[MetodoPagamentoOut])
def listar(db: Session = Depends(get_db)):
    return db.query(metodo_pagamento).all()

#Buscar por id da classe
@router.get("/{id}", response_model=MetodoPagamentoOut)
def buscar(id: int, db: Session = Depends(get_db)):
    novo = db.query(metodo_pagamento).get(id)
    if not novo:
        raise HTTPException(status_code=404, detail="Metodo de pagamento não encontrada")
    return novo


@router.put("/{id}", response_model=MetodoPagamentoOut)
def atualizar(id: int, dados: MetodoPagamentoCreate, db: Session = Depends(get_db)):
    novo = db.query(metodo_pagamento).get(id)
    if not novo:
        raise HTTPException(status_code=404, detail="metodo de pagamento não encontrada")

    for campo, valor in dados.model_dump().items():
        setattr(novo, campo, valor)

    db.commit()
    db.refresh(novo)
    return novo

#Deletar a classe
@router.delete("/{id}")
def deletar(id: int, db: Session = Depends(get_db)):
    novo = db.query(metodo_pagamento).get(id)
    if not novo:
        raise HTTPException(status_code=404, detail="Metodo de pagamento não encontrada")

    db.delete(novo)
    db.commit()
    return {"ok": True}