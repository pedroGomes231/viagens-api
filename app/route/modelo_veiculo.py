from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.modelo_veiculo import ModeloVeiculo
from app.schema.modelo_veiculo import ModeloVeiculoCreate , ModeloVeiculoOut

router = APIRouter(prefix="/medelo_veiculo",tags=["MOdelo Veiculo"])


@router.post("/", response_model=ModeloVeiculoOut)
def criar(dados: ModeloVeiculoCreate, db: Session = Depends(get_db)):
    novo = ModeloVeiculo(**dados.model_dump())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

#Listar todas as classes
@router.get("/", response_model=list[ModeloVeiculoOut])
def listar(db: Session = Depends(get_db)):
    return db.query(ModeloVeiculo).all()

#Buscar por id da classe
@router.get("/{id}", response_model=ModeloVeiculoOut)
def buscar(id: int, db: Session = Depends(get_db)):
    novo = db.query(ModeloVeiculo).get(id)
    if not novo:
        raise HTTPException(status_code=404, detail="Classe não encontrada")
    return novo


@router.put("/{id}", response_model=ModeloVeiculoOut)
def atualizar(id: int, dados: ModeloVeiculoCreate, db: Session = Depends(get_db)):
    novo = db.query(ModeloVeiculo).get(id)
    if not novo:
        raise HTTPException(status_code=404, detail="Classe não encontrada")

    for campo, valor in dados.model_dump().items():
        setattr(novo, campo, valor)

    db.commit()
    db.refresh(novo)
    return novo

#Deletar a classe
@router.delete("/{id}")
def deletar(id: int, db: Session = Depends(get_db)):
    novo = db.query(ModeloVeiculo).get(id)
    if not novo:
        raise HTTPException(status_code=404, detail="Classe não encontrada")

    db.delete(novo)
    db.commit()
    return {"ok": True}