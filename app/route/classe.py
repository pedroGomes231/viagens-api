from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.classe import Classe
from app.schema.classe import ClasseSchema

classe = APIRouter()

@classe.post("/")
async def criar_classe(dados: ClasseSchema, db: Session = Depends(get_db)):
    nova_classe = Classe(**dados.model_dump())
    db.add(nova_classe)
    db.commit()
    db.refresh(nova_classe)
    return nova_classe

@classe.get("/")
async def listar_classe(db: Session = Depends(get_db)):
    return db.query(Classe).all()

@classe.delete("/{id}/delete")
async def deletar_classe(id: int, db: Session = Depends(get_db)):
    classe_encontrada = db.query(Classe).filter(Classe.id_classe == id).first()
    
    if not classe_encontrada:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            detail = f"a classe com id {id} nao foi encontrada.")
    
    db.delete(classe_encontrada)
    db.commit()
    
    return {"classe deletada com sucesso"}

@classe.put("/{id}")
async def atualizar_classe(id: int, dados: ClasseSchema = Depends(), db: Session = Depends(get_db)):
    classe_encontrada = db.query(Classe).filter(Classe.id_classe == id).first()

    if not classe_encontrada:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"classe com {id} nao encontrada",
        )       
    
    dados_atualizados = dados.model_dump(exclude_unset=True)

    for chave, valor in dados_atualizados.items():
        setattr(classe_encontrada, chave, valor)

    db.commit()
    db.refresh(classe_encontrada)
    return classe_encontrada