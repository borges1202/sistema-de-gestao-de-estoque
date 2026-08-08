from pydantic import BaseModel
from datetime import datetime


class CategoriaValidation(BaseModel):
    nome: str
    descricao: str


class CategoriaResponse(BaseModel):
    id: int
    nome: str
    descricao: str
    ativo: bool
    criado_em: datetime
