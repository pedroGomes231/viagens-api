from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.metodo_pagamento import MetodoPagamento
from app.schema.metodo_pagamento import MetodoPagamentoSchema

metodo_pagamento = APIRouter()

@metodo_pagamento.post("/")
async def criar_metodo_pagamento(dados: MetodoPagamentoSchema, db: Session = Depends(get_db)):
    novo_metodo = MetodoPagamento(**dados.model_dump())
    db.add(novo_metodo)
    db.commit()
    db.refresh(novo_metodo)
    return novo_metodo

@metodo_pagamento.get("/")
async def listar_metodo_pagamento(db: Session = Depends(get_db)):
    return db.query(MetodoPagamento).all()

@metodo_pagamento.delete("/{id}/delete")
async def deletar_metodo_pagamento(id: int, db: Session = Depends(get_db)):
    metodo_encontrado = db.query(MetodoPagamento).filter(MetodoPagamento.id_metodo_pagamento == id).first()
    
    if not metodo_encontrado:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            detail = f"o metodo de pagamento com id {id} nao foi encontrado.")
    
    db.delete(metodo_encontrado)
    db.commit()
    
    return {"metodo de pagamento deletado com sucesso"}

@metodo_pagamento.put("/{id}")
async def atualizar_metodo_pagamento(id: int, dados: MetodoPagamentoSchema = Depends(), db: Session = Depends(get_db)):
    metodo_encontrado = db.query(MetodoPagamento).filter(MetodoPagamento.id_metodo_pagamento == id).first()

    if not metodo_encontrado:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"metodo de pagamento com {id} nao encontrado",
        )       
    
    dados_atualizados = dados.model_dump(exclude_unset=True)

    for chave, valor in dados_atualizados.items():
        setattr(metodo_encontrado, chave, valor)

    db.commit()
    db.refresh(metodo_encontrado)
    return metodo_encontrado