# Sistema de Gestão de Estoque

API REST desenvolvida com **FastAPI** e **SQLite** para gerenciamento de estoque. O projeto está sendo desenvolvido com foco em boas práticas de arquitetura, validação de dados e organização do código.

## Tecnologias

- Python 3
- FastAPI
- SQLite
- Pydantic
- Uvicorn

## Estrutura do Projeto

```
app/
├── database/
│   ├── connection.py
│   └── database.db
├── routers/
│   └── categorias.py
├── schemas/
│   └── categoria.py
└── main.py
```

## Funcionalidades Implementadas

### Categorias

- Criar categoria
- Listar todas as categorias
- Buscar categoria por ID
- Atualizar categoria
- Excluir categoria

### Validações

- Validação de entrada utilizando Pydantic.
- Respostas padronizadas com `CategoriaResponse`.
- Tratamento de exceções utilizando `HTTPException`.
- Tratamento de erros do SQLite (`IntegrityError` e `OperationalError`).
- Fechamento seguro das conexões com o banco utilizando `try`, `except` e `finally`.
- Suporte a chaves estrangeiras (`PRAGMA foreign_keys = ON`).

## Status HTTP utilizados

| Método | Endpoint | Status |
|---------|----------|--------|
| POST | `/categorias` | 201 Created |
| GET | `/categorias` | 200 OK |
| GET | `/categorias/{id}` | 200 OK / 404 Not Found |
| PUT | `/categorias/{id}` | 200 OK / 404 Not Found / 409 Conflict |
| DELETE | `/categorias/{id}` | 204 No Content / 404 Not Found / 409 Conflict |

## Próximos passos

- CRUD de Produtos
- CRUD de Usuários
- CRUD de Movimentações
- Autenticação
- Testes automatizados
- Docker