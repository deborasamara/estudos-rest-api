from typing import Union

from fastapi import FastAPI

app = FastAPI()

vendas = {
    1: {"item": "lata", "preco_unitario": 4, "quantidade": 5},
    2: {"item": "garrafa 2L", "preco_unitario": 35, "quantidade": 10},
    3: {"item": "lata mini", "preco_unitario": 2, "quantidade": 5},
}


@app.get("/")
def home():
    return {"vendas": len(vendas)}


@app.get("/vendas/{id_venda}")
def pegar_venda(id_venda:int): # automaticamente faz uma validação
    if id_venda in vendas:
        return vendas[id_venda]
    else:
        return {"Erro": "ID Venda inexistente"}