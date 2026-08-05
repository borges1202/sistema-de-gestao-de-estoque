# Sistema de Gestão de Estoque

API REST desenvolvida com **FastAPI** para gerenciamento de estoque, permitindo o cadastro de categorias, produtos e movimentações de entrada e saída, mantendo o histórico completo das operações.

> Projeto desenvolvido com foco em boas práticas de organização, validação de dados e regras de negócio.

---

# Tecnologias

- Python 3.13+
- FastAPI
- Pydantic
- SQLite
- Uvicorn
- Git
- GitHub

---

# Funcionalidades

## Categorias

- Cadastro de categorias
- Listagem de categorias
- Consulta por ID
- Atualização
- Exclusão
- Validação de dados
- Response Models

---

## Produtos

- Cadastro de produtos
- Listagem de produtos
- Consulta por ID
- Atualização
- Exclusão
- SKU único
- Controle de estoque mínimo
- Validação de categoria

---

## Movimentações

- Registro de entrada
- Registro de saída
- Atualização automática do estoque
- Histórico de movimentações
- Registro do responsável
- Validação de produto ativo
- Bloqueio de estoque insuficiente
- Controle transacional (`commit` / `rollback`)

---

# Estrutura do Projeto

```text
estoque/
│
├── app/
│   ├── database/
│   │   ├── connection.py
│   │   ├── init_db.py
│   │   └── database.db
│   │
│   ├── routers/
│   │   ├── categorias.py
│   │   ├── produtos.py
│   │   └── movimentacoes.py
│   │
│   ├── schemas/
│   │   ├── categoria.py
│   │   ├── produto.py
│   │   └── movimentacoes.py
│   │
│   └── main.py
│
├── docs/
│   ├── PRD.md
│   ├── DATABASE.md
│   └── ARCHITECTURE.md
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Arquitetura

```text
Cliente
    │
    ▼
FastAPI (Routers)
    │
    ▼
Schemas (Validação)
    │
    ▼
Regras de Negócio
    │
    ▼
SQLite
```

---

# Banco de Dados

Atualmente o sistema possui três entidades principais:

- Categorias
- Produtos
- Movimentações

Relacionamentos:

```text
Categoria
     │
     │ 1:N
     ▼
 Produto
     │
     │ 1:N
     ▼
Movimentação
```

---

# Regras de Negócio

- SKU deve ser único.
- Todo produto pertence a uma categoria existente.
- Produtos inativos não podem receber movimentações.
- Não é permitido estoque negativo.
- Toda movimentação registra:
  - Produto
  - Usuário
  - Tipo
  - Quantidade
  - Estoque anterior
  - Estoque atual
  - Observação
  - Data e horário

---

# Como executar

Clone o projeto:

```bash
git clone https://github.com/borges1202/sistema-de-gestao-de-estoque.git
```

Entre na pasta:

```bash
cd sistema-de-gestao-de-estoque
```

Crie o ambiente virtual:

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Linux/macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute a aplicação:

```bash
uvicorn app.main:app --reload
```

Acesse:

```
http://127.0.0.1:8000/docs
```

---

# Próximas funcionalidades

- CRUD de usuários
- Soft Delete de produtos
- Soft Delete de categorias
- Autenticação JWT
- Controle de permissões
- Testes automatizados
- Docker
- PostgreSQL

---

# Status do Projeto

| Módulo | Status |
|---------|--------|
| Categorias | Concluído |
| Produtos | Concluído |
| Movimentações | Concluído |
| Usuários | Em desenvolvimento |
| Autenticação | Planejado |
| Docker | Planejado |
| PostgreSQL | Planejado |

---

# Autor

**Arthur Borges**

- GitHub: https://github.com/borges1202
- LinkedIn: https://www.linkedin.com/in/borgess/