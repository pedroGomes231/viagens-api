from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.avaliacao import Avaliacao
from app.schema.avaliacao import AvaliacaoSchema

avaliacao = APIRouter()

@avaliacao.post("/")
async def criar_avaliacao(dados: AvaliacaoSchema, db: Session = Depends(get_db)):
    nova_avaliacao = Avaliacao(**dados.model_dump())
    db.add(nova_avaliacao)
    db.commit()
    db.refresh(nova_avaliacao)
    return nova_avaliacao

@avaliacao.get("/")
async def listar_avaliacao(db: Session = Depends(get_db)):
    return db.query(Avaliacao).all()

@avaliacao.delete("/{id}/delete")
async def deletar_avaliacao(id: int, db: Session = Depends(get_db)):
    avaliacao_encontrada = db.query(Avaliacao).filter(Avaliacao.id == id).first()
    
    if not avaliacao_encontrada:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            detail = f"a avaliacao com id {id} nao foi encontrada.")
    
    db.delete(avaliacao_encontrada)
    db.commit()
    
    return {"avaliacao deletada com sucesso"}

@avaliacao.put("/{id}")
async def atualizar_avaliacao(id: int, dados: AvaliacaoSchema = Depends(), db: Session = Depends(get_db)):
    avaliacao_encontrada = db.query(Avaliacao).filter(Avaliacao.id == id).first()

    if not avaliacao_encontrada:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"avaliacao com {id} nao encontrada",
        )       
    
    dados_atualizados = dados.model_dump(exclude_unset=True)

    for chave, valor in dados_atualizados.items():
        setattr(avaliacao_encontrada, chave, valor)

    db.commit()
    db.refresh(avaliacao_encontrada)
    return avaliacao_encontrada