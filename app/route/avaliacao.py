from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.avaliacao import Avaliacao
from app.schema.avaliacao import AvaliacaoCreate, AvaliacaoOut

router = APIRouter(prefix="/avaliacoes",tags=["Avaliacoes"])

# Criar
@router.post("/", response_model=AvaliacaoOut)
def criar(dados: AvaliacaoCreate, db: Session = Depends(get_db)):
    novo = Avaliacao(**dados.model_dump())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

# Listar todos
@router.get("/", response_model=list[AvaliacaoOut])
def listar(db: Session = Depends(get_db)):
    return db.query(Avaliacao).all()

# Buscar por ID
@router.get("/{id}", response_model=AvaliacaoOut)
def buscar(id: int, db: Session = Depends(get_db)):
    novo = db.query(Avaliacao).get(id)
    if not novo:
        raise HTTPException(status_code=404, detail="Avaliação não encontrada")
    return novo

# Atualizar
@router.put("/{id}", response_model=AvaliacaoOut)
def atualizar(id: int, dados: AvaliacaoCreate, db: Session = Depends(get_db)):
    novo = db.query(Avaliacao).get(id)
    if not novo:
        raise HTTPException(status_code=404, detail="Avaliação não encontrada")

    for campo, valor in dados.model_dump().items():
        setattr(novo, campo, valor)

    db.commit()
    db.refresh(novo)
    return novo

# Deletar
@router.delete("/{id}")
def deletar(id: int, db: Session = Depends(get_db)):
    novo = db.query(Avaliacao).get(id)
    if not novo:
        raise HTTPException(status_code=404, detail="Avaliação não encontrada")

    db.delete(novo)
    db.commit()
    return {"ok": True}