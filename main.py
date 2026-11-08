from fastapi import FastAPI, HTTPException
from models import EntradaTraducao, SaidaTraducao
from traducao import traduzir_texto

app = FastAPI(title="TP2 - Tradução de inglês para francês")


@app.post("/traduzir", response_model=SaidaTraducao)
def traduzir(dados: EntradaTraducao):
    try:
        traducao = traduzir_texto(dados.texto)
    except ValueError as erro:
        raise HTTPException(status_code=400, detail=(erro))
    return {"texto_original": dados.texto, "texto_traduzido": traducao}
