from fastapi import FastAPI

from app.routers import categorias
from app.routers import produtos
from app.routers import movimentacoes
from app.routers import usuarios

app = FastAPI()

@app.get('/')
def inicio():
    return {'mensagem': 'API de estoque funcionando'}

app.include_router(categorias.router)
app.include_router(produtos.router)
app.include_router(movimentacoes.router)
app.include_router(usuarios.router)