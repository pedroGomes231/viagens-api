from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.modelo_veiculo import ModeloVeiculo
from app.schema.modelo_veiculo import ModeloVeiculoSchema

modelo_veiculo = APIRouter()

@modelo_veiculo.post("/")
async def criar_modelo_veiculo(dados: ModeloVeiculoSchema, db: Session = Depends(get_db)):
    novo_modelo = ModeloVeiculo(**dados.model_dump())
    db.add(novo_modelo)
    db.commit()
    db.refresh(novo_modelo)
    return novo_modelo

@modelo_veiculo.get("/")
async def listar_modelo_veiculo(db: Session = Depends(get_db)):
    return db.query(ModeloVeiculo).all()

@modelo_veiculo.delete("/{id}/delete")
async def deletar_modelo_veiculo(id: int, db: Session = Depends(get_db)):
    modelo_encontrado = db.query(ModeloVeiculo).filter(ModeloVeiculo.id_modelo == id).first()
    
    if not modelo_encontrado:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            detail = f"o modelo de veiculo com id {id} nao foi encontrado.")
    
    db.delete(modelo_encontrado)
    db.commit()
    
    return {"modelo de veiculo deletado com sucesso"}

@modelo_veiculo.put("/{id}")
async def atualizar_modelo_veiculo(id: int, dados: ModeloVeiculoSchema, db: Session = Depends(get_db)):
    modelo_encontrado = db.query(ModeloVeiculo).filter(ModeloVeiculo.id_modelo == id).first()

    if not modelo_encontrado:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"modelo de veiculo com {id} nao encontrado",
        )       
    
    dados_atualizados = dados.model_dump(exclude_unset=True)

    for chave, valor in dados_atualizados.items():
        setattr(modelo_encontrado, chave, valor)

    db.commit()
    db.refresh(modelo_encontrado)
    return modelo_encontrado