from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.tipo_combustivel import TipoCombustivel
from app.schema.tipo_combustivel import TipoCombustivelSchema

tipo_combustivel = APIRouter()

@tipo_combustivel.post("/")
async def criar_tipo_combustivel(dados: TipoCombustivelSchema, db: Session = Depends(get_db)):
    novo_combustivel = TipoCombustivel(**dados.model_dump())
    db.add(novo_combustivel)
    db.commit()
    db.refresh(novo_combustivel)
    return novo_combustivel

@tipo_combustivel.get("/")
async def listar_tipo_combustivel(db: Session = Depends(get_db)):
    return db.query(TipoCombustivel).all()

@tipo_combustivel.delete("/{id}/delete")
async def deletar_tipo_combustivel(id: int, db: Session = Depends(get_db)):
    combustivel_encontrado = db.query(TipoCombustivel).filter(TipoCombustivel.id_combustivel == id).first()
    
    if not combustivel_encontrado:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            detail = f"o tipo de combustivel com id {id} nao foi encontrado.")
    
    db.delete(combustivel_encontrado)
    db.commit()
    
    return {"tipo de combustivel deletado com sucesso"}

@tipo_combustivel.put("/{id}")
async def atualizar_tipo_combustivel(id: int, dados: TipoCombustivelSchema = Depends(), db: Session = Depends(get_db)):
    combustivel_encontrado = db.query(TipoCombustivel).filter(TipoCombustivel.id_combustivel == id).first()

    if not combustivel_encontrado:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"tipo de combustivel com {id} nao encontrado",
        )       
    
    dados_atualizados = dados.model_dump(exclude_unset=True)

    for chave, valor in dados_atualizados.items():
        setattr(combustivel_encontrado, chave, valor)

    db.commit()
    db.refresh(combustivel_encontrado)
    return combustivel_encontrado