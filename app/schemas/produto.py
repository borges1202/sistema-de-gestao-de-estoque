from pydantic import BaseModel, Field
from datetime import datetime


class ProdutoCreate(BaseModel):
    nome: str
    sku: str
    descricao: str | None = None
    estoque_minimo: int = Field(default=0, ge=0)
    categoria_id: int


class ProdutoResponse(BaseModel):
    id: int
    nome: str
    sku: str
    descricao: str | None
    quantidade: int
    estoque_minimo: int
    categoria_id: int
    ativo: bool
    criado_em: datetime
    atualizado_em: datetime


class ProdutoUpdate(BaseModel):
    nome: str
    descricao: str | None = None
    estoque_minimo: int = Field(default=0, ge=0)
    categoria_id: int

class ProdutoStatusPatch(BaseModel):
    ativo: bool
