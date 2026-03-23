from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.servico import Servico
from app.schema.servico import ServicoSchema

servico = APIRouter()

@servico.post("/")
async def criar_servico(dados: ServicoSchema, db: Session = Depends(get_db)):
    novo_servico = Servico(**dados.model_dump())
    db.add(novo_servico)
    db.commit()
    db.refresh(novo_servico)
    return novo_servico

@servico.get("/")
async def listar_servico(db: Session = Depends(get_db)):
    return db.query(Servico).all()

@servico.delete("/{id}/delete")
async def deletar_servico(id: int, db: Session = Depends(get_db)):
    servico_encontrado = db.query(Servico).filter(Servico.id_servico == id).first()
    
    if not servico_encontrado:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            detail = f"o servico com id {id} nao foi encontrado.")
    
    db.delete(servico_encontrado)
    db.commit()
    
    return {"servico deletado com sucesso"}

@servico.put("/{id}")
async def atualizar_servico(id: int, dados: ServicoSchema = Depends(), db: Session = Depends(get_db)):
    servico_encontrado = db.query(Servico).filter(Servico.id_servico == id).first()

    if not servico_encontrado:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"servico com {id} nao encontrado",
        )       
    
    dados_atualizados = dados.model_dump(exclude_unset=True)

    for chave, valor in dados_atualizados.items():
        setattr(servico_encontrado, chave, valor)

    db.commit()
    db.refresh(servico_encontrado)
    return servico_encontrado