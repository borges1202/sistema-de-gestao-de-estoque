from pydantic import BaseModel, Field
from datetime import datetime
from typing import Literal


class MovimentacoesCreate(BaseModel):
    produto_id: int
    usuario_id: int
    tipo: Literal["ENTRADA", "SAIDA"]
    quantidade: int = Field(gt=0)
    observacao: str | None = None


class MovimentacoesResponse(BaseModel):
    id: int
    produto_id: int
    usuario_id: int
    tipo: Literal["ENTRADA", "SAIDA"]
    quantidade: int = Field(gt=0)
    estoque_anterior: int
    estoque_atual: int
    observacao: str | None = None
    criado_em: datetime
