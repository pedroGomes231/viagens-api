from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.veiculo import Veiculo
from app.schema.veiculo import VeiculoSchema

veiculo = APIRouter()

@veiculo.post("/")
async def criar_veiculo(dados: VeiculoSchema, db: Session = Depends(get_db)):
    novo_veiculo = Veiculo(**dados.model_dump())
    db.add(novo_veiculo)
    db.commit()
    db.refresh(novo_veiculo)
    return novo_veiculo

@veiculo.get("/")
async def listar_veiculo(db: Session = Depends(get_db)):
    return db.query(Veiculo).all()

@veiculo.delete("/{id}/delete")
async def deletar_veiculo(id: int, db: Session = Depends(get_db)):
    veiculo_encontrado = db.query(Veiculo).filter(Veiculo.id_veiculo == id).first()
    
    if not veiculo_encontrado:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail = f"o veiculo com id {id} nao foi encontrado.")
    
    db.delete(veiculo_encontrado)
    db.commit()
    return {"veiculo deletado com sucesso"}

@veiculo.put("/{id}")
async def atualizar_veiculo(id: int, dados: VeiculoSchema, db: Session = Depends(get_db)):
    veiculo_encontrado = db.query(Veiculo).filter(Veiculo.id_veiculo == id).first()

    if not veiculo_encontrado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"veiculo com {id} nao encontrado")       
    
    dados_atualizados = dados.model_dump(exclude_unset=True)
    for chave, valor in dados_atualizados.items():
        setattr(veiculo_encontrado, chave, valor)

    db.commit()
    db.refresh(veiculo_encontrado)
    return veiculo_encontrado