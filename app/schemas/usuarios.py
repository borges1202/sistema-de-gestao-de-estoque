from pydantic import BaseModel, Field
from datetime import datetime

class UsuarioCreate(BaseModel):
    nome: str = Field(min_length=3, max_length=30)
    cpf: str = Field(pattern=r"^\d+$", min_length=11, max_length=11)
    telefone: str = Field(pattern=r"^\d+$", min_length=13, max_length=13)

class UsuarioResponse(BaseModel):
    id: int
    nome: str
    cpf: str
    telefone: str
    ativo: bool
    criado_em: datetime

class UsuarioUpdate(BaseModel):
    nome: str = Field(min_length=3, max_length=30)
    telefone: str = Field(pattern=r"^\d+$", min_length=13, max_length=13)

class UsuarioStatusPatch(BaseModel):
    ativo:bool