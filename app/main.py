from fastapi import FastAPI
from app.database import Base, engine
from app.route.pagamento import pagamento
from app.route.usuario import usuario
from app.route.corrida import corrida
from app.route.veiculo import veiculo
from app.route.passageiro import passageiro
from app.route.motorista import motorista
from app.route.motorista_veiculo import motorista_veiculo
from app.route.avaliacao import avaliacao
from app.route.servico import servico
from app.route.classe import classe
from app.route.tipo_combustivel import tipo_combustivel
from app.route.modelo_veiculo import modelo_veiculo
from app.route.metodo_pagamento import metodo_pagamento

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(usuario, prefix="/usuarios", tags=["Usuários"])
app.include_router(passageiro, prefix="/passageiros", tags=["Passageiros"])
app.include_router(motorista, prefix="/motoristas", tags=["Motoristas"])
app.include_router(veiculo, prefix="/veiculos", tags=["Veículos"])
app.include_router(modelo_veiculo, prefix="/modelo_veiculo", tags=["Modelos de Veículos"])
app.include_router(motorista_veiculo, prefix="/motorista_veiculo", tags=["Vínculo Motorista-Veículo"])
app.include_router(corrida, prefix="/corridas", tags=["Corridas"])
app.include_router(pagamento, prefix="/pagamentos", tags=["Pagamentos"])
app.include_router(metodo_pagamento, prefix="/metodos_pagamento", tags=["Métodos de Pagamento"])
app.include_router(avaliacao, prefix="/avaliacoes", tags=["Avaliações"])
app.include_router(servico, prefix="/servicos", tags=["Serviços"])
app.include_router(classe, prefix="/classes", tags=["Classes"])
app.include_router(tipo_combustivel, prefix="/tipos_combustivel", tags=["Tipos de Combustível"])

@app.get("/")
async def health_check():
    return{"status": "API online!"}