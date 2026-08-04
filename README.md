# Sistema de Gestão de Estoque

API REST desenvolvida com FastAPI e SQLite para gerenciamento de estoque, construída com foco em organização, boas práticas e escalabilidade.

## Tecnologias

- Python 3
- FastAPI
- SQLite
- Pydantic
- Uvicorn

## Funcionalidades

### Categorias

- Criar categoria
- Listar categorias
- Buscar categoria por ID
- Atualizar categoria
- Excluir categoria
- Tratamento de exceções
- Response Models
- Validação de dados

### Produtos

- Criar produto
- Listar produtos
- Buscar produto por ID
- Atualizar produto
- Excluir produto
- Validação de categoria existente
- SKU único
- Normalização automática do SKU para maiúsculas
- Estoque mínimo validado
- Response Models
- Tratamento de exceções

## Status HTTP

| Código | Descrição |
|---------|-----------|
| 200 | Requisição realizada com sucesso |
| 201 | Recurso criado |
| 204 | Recurso removido |
| 404 | Recurso não encontrado |
| 409 | Conflito de dados |
| 422 | Erro de validação |
| 500 | Erro interno do servidor |

## Estrutura

```
app/
├── database/
├── routers/
│   ├── categorias.py
│   └── produtos.py
├── schemas/
│   ├── categoria.py
│   └── produto.py
└── main.py
```

## Próximas etapas

- Movimentações de estoque
- Controle de usuários
- Histórico de movimentações
- Autenticação
- Testes automatizados
- Docker