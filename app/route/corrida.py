from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.corrida import Corrida
from app.schema.corrida import CorridaSchema

corrida = APIRouter()

@corrida.post("/")
async def criar_corrida(dados: CorridaSchema, db: Session = Depends(get_db)):
    nova_corrida = Corrida(**dados.model_dump())
    db.add(nova_corrida)
    db.commit()
    db.refresh(nova_corrida)
    return nova_corrida

@corrida.get("/")
async def listar_corrida(db: Session = Depends(get_db)):
    return db.query(Corrida).all()

@corrida.delete("/{id}/delete")
async def deletar_corrida(id: int, db: Session = Depends(get_db)):
    corrida_encontrada = db.query(Corrida).filter(Corrida.id_corrida == id).first()
    
    if not corrida_encontrada:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail = f"a corrida com id {id} nao foi encontrada.")
    
    db.delete(corrida_encontrada)
    db.commit()
    return {"corrida deletada com sucesso"}

@corrida.put("/{id}")
async def atualizar_corrida(id: int, dados: CorridaSchema = Depends(), db: Session = Depends(get_db)):
    corrida_encontrada = db.query(Corrida).filter(Corrida.id_corrida == id).first()

    if not corrida_encontrada:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"corrida com {id} nao encontrada")       
    
    dados_atualizados = dados.model_dump(exclude_unset=True)
    for chave, valor in dados_atualizados.items():
        setattr(corrida_encontrada, chave, valor)

    db.commit()
    db.refresh(corrida_encontrada)
    return corrida_encontrada