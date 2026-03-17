from fastapi import FastAPI
from app.database import Base, engine

# desse jeito ela importa todas as rotas
from app.route import (
    usuario,
    passageiro,
    motorista,
    veiculo,
    corrida,
    avaliacao,
    pagamento,
    metodo_pagamento,
    modelo_veiculo,
    motorista_veiculo,
    servico,
    tipo_combustivel,
    classe,
)

Base.metadata.create_all(bind=engine)

app = FastAPI()

# aq eela registra todas as rotas
app.include_router(usuario.router)
app.include_router(passageiro.router)
app.include_router(motorista.router)
app.include_router(veiculo.router)
app.include_router(corrida.router)
app.include_router(avaliacao.router)
app.include_router(pagamento.router)
app.include_router(metodo_pagamento.router)
app.include_router(modelo_veiculo.router)
app.include_router(motorista_veiculo.router)
app.include_router(servico.router)
app.include_router(tipo_combustivel.router)
app.include_router(classe.router)