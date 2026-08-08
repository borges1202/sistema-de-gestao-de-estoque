# Sistema de Gestão de Estoque

API REST para gerenciamento de estoque desenvolvida com **Python e FastAPI**, permitindo o controle de categorias, produtos, usuários e movimentações de entrada e saída.

O projeto foi desenvolvido com foco no aprendizado e aplicação de conceitos de desenvolvimento Back-End, incluindo regras de negócio, validação de dados, persistência, integridade referencial, transações e organização em camadas.

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
- Validação de dados
- Validação de relacionamentos com produtos

### Produtos

- Cadastro de produtos
- Listagem de produtos
- Consulta por ID
- Atualização
- SKU único
- Controle de estoque mínimo
- Validação de categoria
- Ativação e desativação
- Soft Delete
- Preservação do histórico após desativação

### Usuários

- Cadastro de usuários
- Listagem de usuários
- Consulta por ID
- Atualização de nome e telefone
- CPF obrigatório e único
- Validação de CPF
- Ativação e desativação via `PATCH`
- Bloqueio de movimentações para usuários inativos
- Preservação do histórico após desativação

### Movimentações

- Registro de entradas
- Registro de saídas
- Atualização automática do estoque
- Histórico de movimentações
- Registro do usuário responsável
- Registro do estoque anterior e atual
- Validação de produto
- Validação de usuário
- Bloqueio de produtos inativos
- Bloqueio de usuários inativos
- Bloqueio de saídas com estoque insuficiente
- Controle transacional com `commit` e `rollback`

---

## Arquitetura

O projeto utiliza separação entre a camada HTTP e o acesso aos dados.

```text
Cliente
    │
    ▼
FastAPI
    │
    ▼
Routers
    │
    ▼
Repositories
    │
    ▼
SQLite
```

### Routers

Responsáveis por:

- receber as requisições HTTP;
- utilizar os schemas;
- aplicar as regras de negócio;
- controlar respostas e status HTTP;
- coordenar as operações da aplicação.

### Repositories

Responsáveis pelo acesso aos dados:

- `SELECT`
- `INSERT`
- `UPDATE`
- consultas ao SQLite;
- retorno dos resultados para os routers.

Essa separação evita que as rotas dependam diretamente das instruções SQL e facilita a manutenção do projeto.

### Schemas

Os schemas Pydantic são responsáveis pela validação e estrutura dos dados de entrada e saída da API.

---

## Estrutura do Projeto

```text
sistema-de-gestao-de-estoque/
│
├── app/
│   │
│   ├── database/
│   │   ├── connection.py
│   │   ├── init_db.py
│   │   └── database.db
│   │
│   ├── repositories/
│   │   ├── __init__.py
│   │   ├── categoria_repository.py
│   │   ├── produto_repository.py
│   │   ├── usuario_repository.py
│   │   └── movimentacao_repository.py
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

## Banco de Dados

O sistema possui quatro entidades principais:

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

As Foreign Keys são utilizadas para preservar a integridade dos relacionamentos.

---

## Regras de Negócio

### Produtos

- Nome obrigatório
- SKU único
- Produto deve pertencer a uma categoria existente
- Estoque não pode ficar negativo
- Produtos podem ser desativados
- Produtos inativos não podem receber movimentações
- Produtos com histórico não são removidos fisicamente

### Usuários

- Nome obrigatório
- CPF obrigatório
- CPF deve possuir 11 dígitos numéricos
- CPF deve ser único
- Telefone obrigatório
- CPF não pode ser alterado pelo endpoint de atualização
- Usuários podem ser ativados e desativados
- Usuários inativos não podem realizar movimentações
- A desativação não remove o histórico do usuário

### Movimentações

Toda movimentação registra:

- produto;
- usuário responsável;
- tipo;
- quantidade;
- estoque anterior;
- estoque atual;
- observação;
- data e horário.

Tipos disponíveis:

```text
ENTRADA
SAIDA
```

Uma saída somente é permitida quando existe estoque suficiente.

A atualização do estoque e o registro da movimentação fazem parte da mesma operação, utilizando transações para preservar a consistência dos dados.

---

## Principais Endpoints

### Categorias

```text
POST   /categorias
GET    /categorias
GET    /categorias/{id}
PUT    /categorias/{id}
```

### Produtos

```text
POST   /produtos
GET    /produtos
GET    /produtos/{id}
PUT    /produtos/{id}
PATCH  /produtos/{id}/status
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

A documentação interativa completa pode ser consultada pelo Swagger.

---

## Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/borges1202/sistema-de-gestao-de-estoque.git
```

### 2. Entre no projeto

```bash
cd sistema-de-gestao-de-estoque
```

### 3. Crie um ambiente virtual

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

### 6. Acesse a documentação

```text
http://127.0.0.1:8000/docs
```

---

## Status do Projeto

| Módulo | Status |
| --- | --- |
| Categorias | Concluído |
| Produtos | Concluído |
| Usuários | Concluído |
| Movimentações | Concluído |
| Repositories | Concluído |
| Soft Delete de Produtos | Concluído |
| Soft Delete de Categorias | Planejado |
| Testes Automatizados | Planejado |
| Autenticação JWT | Planejado |
| Controle de Permissões | Planejado |
| PostgreSQL | Planejado |
| Docker | Planejado |
| Deploy | Planejado |

---

## Roadmap

### Concluído

- [x] CRUD de categorias
- [x] CRUD de produtos
- [x] CRUD de usuários
- [x] Controle de movimentações
- [x] Controle de entrada e saída de estoque
- [x] Histórico de movimentações
- [x] Ativação e desativação de usuários
- [x] Soft Delete de produtos
- [x] Separação da camada de acesso aos dados com Repositories
- [x] Controle transacional das movimentações

### Próximas etapas

- [ ] Revisar necessidade de uma camada de Services
- [ ] Soft Delete de categorias
- [ ] Testes automatizados
- [ ] Autenticação JWT
- [ ] Controle de permissões
- [ ] Migração para PostgreSQL
- [ ] Docker
- [ ] Deploy

---

## Documentação

A documentação técnica está disponível no diretório `docs/`:

- `PRD.md` — requisitos e escopo do sistema
- `DATABASE.md` — estrutura e relacionamentos do banco
- `ARCHITECTURE.md` — arquitetura e organização do projeto

---

## Autor

**Arthur Borges**

GitHub: `borges1202`  
LinkedIn: `borgess`
