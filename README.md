# Sistema de Gestão de Estoque

API REST desenvolvida com **FastAPI** para gerenciamento de estoque, permitindo o controle de categorias, produtos, usuários e movimentações de entrada e saída.

O projeto tem como objetivo aplicar conceitos de desenvolvimento Back-End, regras de negócio, persistência de dados, arquitetura de APIs REST e boas práticas de desenvolvimento.

---

## Tecnologias

- Python 3.13+
- FastAPI
- Pydantic
- SQLite
- Uvicorn
- Git
- GitHub

---

## Funcionalidades

### Categorias

- Cadastro de categorias
- Listagem de categorias
- Consulta por ID
- Atualização
- Exclusão
- Validação de dados
- Response Models

### Produtos

- Cadastro de produtos
- Listagem de produtos
- Consulta por ID
- Atualização
- Exclusão
- SKU único
- Controle de estoque mínimo
- Validação de categoria

### Usuários

- Cadastro de usuários
- Listagem de usuários
- Consulta por ID
- Atualização de nome e telefone
- CPF obrigatório e único
- Validação de CPF
- Ativação e desativação de usuários via `PATCH`
- Preservação do histórico após desativação
- Bloqueio de movimentações para usuários inativos

### Movimentações

- Registro de entrada
- Registro de saída
- Atualização automática do estoque
- Histórico de movimentações
- Registro do usuário responsável
- Registro do estoque anterior e atual
- Validação de produto
- Validação de usuário
- Bloqueio de movimentações por usuários inativos
- Bloqueio de movimentações em produtos inativos
- Bloqueio de saídas com estoque insuficiente
- Controle transacional com `commit` e `rollback`

---

## Estrutura do Projeto

```text
sistema-de-gestao-de-estoque/
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
│   │   ├── usuarios.py
│   │   └── movimentacoes.py
│   │
│   ├── schemas/
│   │   ├── categoria.py
│   │   ├── produto.py
│   │   ├── usuarios.py
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

## Arquitetura Atual

Atualmente, a aplicação segue o seguinte fluxo:

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

O projeto está passando por uma refatoração gradual para separar o acesso ao banco de dados das rotas através da camada de **Repositories**.

Arquitetura planejada após a refatoração:

```text
Cliente
    │
    ▼
FastAPI (Routers)
    │
    ▼
Repositories
    │
    ▼
SQLite
```

---

## Banco de Dados

Atualmente o sistema possui quatro entidades principais:

- Categorias
- Produtos
- Usuários
- Movimentações

### Relacionamentos

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
    ▲
    │ N:1
    │
Usuário
```

Uma categoria pode possuir vários produtos.

Um produto pode possuir várias movimentações.

Um usuário pode ser responsável por várias movimentações.

---

## Regras de Negócio

### Produtos

- O nome do produto é obrigatório.
- O SKU deve ser único.
- Todo produto deve pertencer a uma categoria existente.
- Produtos inativos não podem receber movimentações.
- O estoque nunca pode ficar negativo.

### Usuários

- Nome é obrigatório.
- CPF é obrigatório.
- CPF deve possuir formato válido.
- CPF deve ser único.
- Telefone é obrigatório.
- CPF não pode ser alterado após o cadastro.
- Usuários podem ser ativados ou desativados.
- Usuários inativos não podem realizar movimentações.
- A desativação de um usuário não remove seu histórico.

### Movimentações

Toda movimentação registra:

- Produto
- Usuário responsável
- Tipo (`ENTRADA` ou `SAIDA`)
- Quantidade
- Estoque anterior
- Estoque atual
- Observação
- Data e horário

Uma saída só pode ser realizada quando houver estoque suficiente.

A atualização do estoque e o registro da movimentação fazem parte da mesma operação, utilizando controle transacional para preservar a consistência dos dados.

---

## Endpoints

### Categorias

```text
POST   /categorias
GET    /categorias
GET    /categorias/{id}
PUT    /categorias/{id}
DELETE /categorias/{id}
```

### Produtos

```text
POST   /produtos
GET    /produtos
GET    /produtos/{id}
PUT    /produtos/{id}
DELETE /produtos/{id}
```

### Usuários

```text
POST   /usuarios
GET    /usuarios
GET    /usuarios/{id}
PUT    /usuarios/{id}
PATCH  /usuarios/{id}/status
```

### Movimentações

```text
POST   /movimentacoes
GET    /movimentacoes
GET    /movimentacoes/{id}
```

A documentação interativa completa dos endpoints está disponível através do Swagger após iniciar a aplicação.

---

## Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/borges1202/sistema-de-gestao-de-estoque.git
```

### 2. Entre no diretório

```bash
cd sistema-de-gestao-de-estoque
```

### 3. Crie o ambiente virtual

#### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

#### Linux/macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 4. Instale as dependências

```bash
pip install -r requirements.txt
```

### 5. Execute a aplicação

```bash
uvicorn app.main:app --reload
```

### 6. Acesse o Swagger

```text
http://127.0.0.1:8000/docs
```

---

## Status do Projeto

| Módulo | Status |
| --- | --- |
| Categorias | Concluído |
| Produtos | Concluído |
| Movimentações | Concluído |
| Usuários | Concluído |
| Refatoração em Repositories | Em desenvolvimento |
| Soft Delete | Planejado |
| Testes automatizados | Planejado |
| Autenticação JWT | Planejado |
| Controle de permissões | Planejado |
| PostgreSQL | Planejado |
| Docker | Planejado |
| Deploy | Planejado |

---

## Roadmap

### Etapa atual

- [x] CRUD de categorias
- [x] CRUD de produtos
- [x] Controle de movimentações
- [x] CRUD de usuários
- [x] Ativação e desativação de usuários
- [x] Integração entre usuários e movimentações
- [ ] Separação da camada de acesso aos dados com Repositories

### Próximas etapas

- [ ] Soft Delete de produtos
- [ ] Soft Delete de categorias
- [ ] Testes automatizados
- [ ] Autenticação JWT
- [ ] Controle de permissões
- [ ] Migração para PostgreSQL
- [ ] Docker
- [ ] Deploy

---

## Documentação

A documentação técnica do projeto está disponível no diretório `docs/`:

- `PRD.md` — requisitos e escopo do produto
- `DATABASE.md` — estrutura do banco de dados
- `ARCHITECTURE.md` — arquitetura e organização do projeto

---

## Autor

**Arthur Borges**

GitHub: `borges1202`  
LinkedIn: `borgess`
