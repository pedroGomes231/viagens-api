from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.motorista_veiculo import MotoristaVeiculo
from app.schema.motorista_veiculo import MotoristaVeiculoCreate, MotoristaVeiculoOut

router = APIRouter(prefix="/motorista_veiculo",tags=["motorista veiculo"])


@router.post("/", response_model=MotoristaVeiculoOut)
def criar(dados: MotoristaVeiculoCreate, db: Session = Depends(get_db)):
    novo = MotoristaVeiculo(**dados.model_dump())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

#Listar todas as classes
@router.get("/", response_model=list[MotoristaVeiculoOut])
def listar(db: Session = Depends(get_db)):
    return db.query(MotoristaVeiculo).all()

#Buscar por id da classe
@router.get("/{id}", response_model=MotoristaVeiculoOut)
def buscar(id: int, db: Session = Depends(get_db)):
    novo = db.query(MotoristaVeiculo).get(id)
    if not novo:
        raise HTTPException(status_code=404, detail="Motorista não encontrado")
    return novo


@router.put("/{id}", response_model=MotoristaVeiculoOut)
def atualizar(id: int, dados: MotoristaVeiculoCreate, db: Session = Depends(get_db)):
    novo = db.query(MotoristaVeiculo).get(id)
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
    novo = db.query(MotoristaVeiculo).get(id)
    if not novo:
        raise HTTPException(status_code=404, detail="MOtorista não encontrado")

    db.delete(novo)
    db.commit()
    return {"ok": True}