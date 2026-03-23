from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.motorista_veiculo import MotoristaVeiculo
from app.schema.motorista_veiculo import MotoristaVeiculoSchema

motorista_veiculo = APIRouter()

@motorista_veiculo.post("/")
async def criar_motorista_veiculo(dados: MotoristaVeiculoSchema, db: Session = Depends(get_db)):
    novo_registro = MotoristaVeiculo(**dados.model_dump())
    db.add(novo_registro)
    db.commit()
    db.refresh(novo_registro)
    return novo_registro

@motorista_veiculo.get("/")
async def listar_motorista_veiculo(db: Session = Depends(get_db)):
    return db.query(MotoristaVeiculo).all()

@motorista_veiculo.delete("/{id_motorista}/{id_veiculo}/delete")
async def deletar_motorista_veiculo(id_motorista: int, id_veiculo: int, db: Session = Depends(get_db)):
    registro_encontrado = db.query(MotoristaVeiculo).filter(
        MotoristaVeiculo.id_motorista == id_motorista,
        MotoristaVeiculo.id_veiculo == id_veiculo
    ).first()
    
    if not registro_encontrado:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Registro não encontrado.")
    
    db.delete(registro_encontrado)
    db.commit()
    return {"registro deletado com sucesso"}

@motorista_veiculo.put("/{id_motorista}/{id_veiculo}")
async def atualizar_motorista_veiculo(id_motorista: int, id_veiculo: int, dados: MotoristaVeiculoSchema = Depends(), db: Session = Depends(get_db)):
    registro_encontrado = db.query(MotoristaVeiculo).filter(
        MotoristaVeiculo.id_motorista == id_motorista,
        MotoristaVeiculo.id_veiculo == id_veiculo
    ).first()

    if not registro_encontrado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Registro não encontrado")       
    
    dados_atualizados = dados.model_dump(exclude_unset=True)
    for chave, valor in dados_atualizados.items():
        setattr(registro_encontrado, chave, valor)

    db.commit()
    db.refresh(registro_encontrado)
    return registro_encontrado