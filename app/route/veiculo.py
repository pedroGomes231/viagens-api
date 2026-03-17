from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.veiculo import Veiculo
from app.schema.veiculo import VeiculoCreate, VeiculoOut

router = APIRouter(prefix="/veiculo",tags=["veiculo"])


@router.post("/", response_model=VeiculoOut)
def criar(dados: VeiculoCreate, db: Session = Depends(get_db)):
    novo = Veiculo(**dados.model_dump())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

#Listar todas as classes
@router.get("/", response_model=list[VeiculoOut])
def listar(db: Session = Depends(get_db)):
    return db.query(Veiculo).all()

#Buscar por id da classe
@router.get("/{id}", response_model=VeiculoOut)
def buscar(id: int, db: Session = Depends(get_db)):
    novo = db.query(Veiculo).get(id)
    if not novo:
        raise HTTPException(status_code=404, detail="Veiculo não encontrado")
    return novo


@router.put("/{id}", response_model=VeiculoOut)
def atualizar(id: int, dados: VeiculoCreate, db: Session = Depends(get_db)):
    novo = db.query(Veiculo).get(id)
    if not novo:
        raise HTTPException(status_code=404, detail=" Veiculo não encontrado")

    for campo, valor in dados.model_dump().items():
        setattr(novo, campo, valor)

    db.commit()
    db.refresh(novo)
    return novo

#Deletar a classe
@router.delete("/{id}")
def deletar(id: int, db: Session = Depends(get_db)):
    obj = db.query(Veiculo).get(id)
    if not obj:
        raise HTTPException(status_code=404, detail="Veiculo não encontrado")

    db.delete(obj)
    db.commit()
    return {"ok": True}