from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.pagamento import Pagamento
from app.schema.pagamento import PagamentoCreate, PagamentoOut

router = APIRouter(prefix="/pagamento",tags=["Pagamento"])


@router.post("/", response_model=PagamentoOut)
def criar(dados: PagamentoCreate, db: Session = Depends(get_db)):
    novo = Pagamento(**dados.model_dump())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

#Listar todas as classes
@router.get("/", response_model=list[PagamentoOut])
def listar(db: Session = Depends(get_db)):
    return db.query(Pagamento).all()

#Buscar por id da classe
@router.get("/{id}", response_model=PagamentoOut)
def buscar(id: int, db: Session = Depends(get_db)):
    novo = db.query(Pagamento).get(id)
    if not novo:
        raise HTTPException(status_code=404, detail="Pagamento não realizado")
    return novo


@router.put("/{id}", response_model=PagamentoOut)
def atualizar(id: int, dados: PagamentoCreate, db: Session = Depends(get_db)):
    novo = db.query(Pagamento).get(id)
    if not novo:
        raise HTTPException(status_code=404, detail="Pagamento não realizado")

    for campo, valor in dados.model_dump().items():
        setattr(novo, campo, valor)

    db.commit()
    db.refresh(novo)
    return novo

#Deletar a classe
@router.delete("/{id}")
def deletar(id: int, db: Session = Depends(get_db)):
    novo = db.query(Pagamento).get(id)
    if not novo:
        raise HTTPException(status_code=404, detail="Pagamento não realizado")

    db.delete(novo)
    db.commit()
    return {"ok": True}