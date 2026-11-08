from pydantic import BaseModel, Field


class EntradaTraducao(BaseModel):
    texto: str = Field(min_length=1)


class SaidaTraducao(BaseModel):
    texto_original: str
    texto_traduzido: str
