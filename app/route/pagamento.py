from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.pagamento import Pagamento
from app.schema.pagamento import PagamentoSchema

pagamento = APIRouter()

@pagamento.post("/")
async def criar_pagamento(dados: PagamentoSchema, db: Session = Depends(get_db)):
    novo_pagamento = Pagamento(**dados.model_dump())
    db.add(novo_pagamento)
    db.commit()
    db.refresh(novo_pagamento)
    return novo_pagamento

@pagamento.get("/")
async def listar_pagamento(db: Session = Depends(get_db)):
    return db.query(Pagamento).all()

@pagamento.delete("/{id}/delete")
async def deletar_pagamento(id: int, db: Session = Depends(get_db)):
    pagamento_encontrado = db.query(Pagamento).filter(Pagamento.id_pagamento == id).first()
    
    if not pagamento_encontrado:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            detail = f"o pagamento com id {id} nao foi encontrado.")
    
    db.delete(pagamento_encontrado)
    db.commit()
    return {"pagamento deletado com sucesso"}

@pagamento.put("/{id}")
async def atualizar_pagamento(id: int, dados: PagamentoSchema = Depends(), db: Session = Depends(get_db)):
    pagamento_encontrado = db.query(Pagamento).filter(Pagamento.id_pagamento == id).first()

    if not pagamento_encontrado:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"pagamento com {id} nao encontrado",
        )       
    
    dados_atualizados = dados.model_dump(exclude_unset=True)
    for chave, valor in dados_atualizados.items():
        setattr(pagamento_encontrado, chave, valor)

    db.commit()
    db.refresh(pagamento_encontrado)
    return pagamento_encontrado