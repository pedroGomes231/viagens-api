from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.motorista import Motorista
from app.schema.motorista import MotoristaSchema

motorista = APIRouter()

@motorista.post("/")
async def criar_motorista(dados: MotoristaSchema, db: Session = Depends(get_db)):
    novo_motorista = Motorista(**dados.model_dump())
    db.add(novo_motorista)
    db.commit()
    db.refresh(novo_motorista)
    return novo_motorista

@motorista.get("/")
async def listar_motorista(db: Session = Depends(get_db)):
    return db.query(Motorista).all()

@motorista.delete("/{id}/delete")
async def deletar_motorista(id: int, db: Session = Depends(get_db)):
    motorista_encontrado = db.query(Motorista).filter(Motorista.id_motorista == id).first()
    
    if not motorista_encontrado:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail = f"o motorista com id {id} nao foi encontrado.")
    
    db.delete(motorista_encontrado)
    db.commit()
    return {"motorista deletado com sucesso"}

@motorista.put("/{id}")
async def atualizar_motorista(id: int, dados: MotoristaSchema, db: Session = Depends(get_db)):
    motorista_encontrado = db.query(Motorista).filter(Motorista.id_motorista == id).first()

    if not motorista_encontrado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"motorista com {id} nao encontrado")       
    
    dados_atualizados = dados.model_dump(exclude_unset=True)
    for chave, valor in dados_atualizados.items():
        setattr(motorista_encontrado, chave, valor)

    db.commit()
    db.refresh(motorista_encontrado)
    return motorista_encontrado