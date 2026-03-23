from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.passageiro import Passageiro
from app.schema.passageiro import PassageiroSchema

passageiro = APIRouter()

@passageiro.post("/")
async def criar_passageiro(dados: PassageiroSchema, db: Session = Depends(get_db)):
    novo_passageiro = Passageiro(**dados.model_dump())
    db.add(novo_passageiro)
    db.commit()
    db.refresh(novo_passageiro)
    return novo_passageiro

@passageiro.get("/")
async def listar_passageiro(db: Session = Depends(get_db)):
    return db.query(Passageiro).all()

@passageiro.delete("/{id}/delete")
async def deletar_passageiro(id: int, db: Session = Depends(get_db)):
    passageiro_encontrado = db.query(Passageiro).filter(Passageiro.id_passageiro == id).first()
    
    if not passageiro_encontrado:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail = f"o passageiro com id {id} nao foi encontrado.")
    
    db.delete(passageiro_encontrado)
    db.commit()
    return {"passageiro deletado com sucesso"}

@passageiro.put("/{id}")
async def atualizar_passageiro(id: int, dados: PassageiroSchema, db: Session = Depends(get_db)):
    passageiro_encontrado = db.query(Passageiro).filter(Passageiro.id_passageiro == id).first()

    if not passageiro_encontrado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"passageiro com {id} nao encontrado")       
    
    dados_atualizados = dados.model_dump(exclude_unset=True)
    for chave, valor in dados_atualizados.items():
        setattr(passageiro_encontrado, chave, valor)

    db.commit()
    db.refresh(passageiro_encontrado)
    return passageiro_encontrado