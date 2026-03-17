from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.classe import Classe
from app.schema.classe import ClasseCreate, ClasseOut

router = APIRouter(prefix="/classe",tags=["classe"])


@router.post("/", response_model=ClasseOut)
def criar(dados: ClasseCreate, db: Session = Depends(get_db)):
    novo = Classe(**dados.model_dump())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

#Listar todas as classes
@router.get("/", response_model=list[ClasseOut])
def listar(db: Session = Depends(get_db)):
    return db.query(Classe).all()

#Buscar por id da classe
@router.get("/{id}", response_model=ClasseOut)
def buscar(id: int, db: Session = Depends(get_db)):
    novo = db.query(Classe).get(id)
    if not novo:
        raise HTTPException(status_code=404, detail="Classe não encontrada")
    return novo


@router.put("/{id}", response_model=ClasseOut)
def atualizar(id: int, dados: ClasseCreate, db: Session = Depends(get_db)):
    novo = db.query(Classe).get(id)
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
    novo = db.query(Classe).get(id)
    if not novo:
        raise HTTPException(status_code=404, detail="Classe não encontrada")

    db.delete(novo)
    db.commit()
    return {"ok": True}