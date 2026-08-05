# Arquitetura do Projeto

## Estrutura de Pastas

```text
estoque/
│
├── app/
│   │
│   ├── main.py
│   │   Inicializa a aplicação FastAPI.
│   │
│   ├── database/
│   │   │
│   │   ├── connection.py
│   │   │   Responsável pela conexão com o banco SQLite.
│   │   │
│   │   ├── init_db.py
│   │   │   Criação das tabelas do banco.
│   │   │
│   │   └── database.db
│   │       Banco de dados SQLite.
│   │
│   ├── routers/
│   │   │
│   │   ├── categorias.py
│   │   │   CRUD de categorias.
│   │   │
│   │   ├── produtos.py
│   │   │   CRUD de produtos.
│   │   │
│   │   └── movimentacoes.py
│   │       Registro e consulta das movimentações de estoque.
│   │
│   └── schemas/
│       │
│       ├── categoria.py
│       ├── produto.py
│       └── movimentacoes.py
│
├── docs/
│   │
│   ├── PRD.md
│   ├── ARCHITECTURE.md
│   └── DATABASE.md
│
├── README.md
├── requirements.txt
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

# Módulos Implementados

## Categorias

- CRUD completo
- Validação de dados
- Tratamento de exceções
- Response Models

## Produtos

- CRUD completo
- SKU único
- Controle de estoque mínimo
- Validação de categoria
- Response Models

## Movimentações

- Registro de entrada
- Registro de saída
- Atualização automática do estoque
- Histórico de movimentações
- Validação de usuário
- Validação de produto ativo
- Bloqueio de estoque insuficiente
- Controle transacional (commit / rollback)

---

# Próximas Evoluções

- CRUD de usuários
- Soft Delete para produtos
- Soft Delete para categorias
- Autenticação JWT
- Controle de permissões
- Testes automatizados
- Docker
- PostgreSQL

---

# Ordem de Desenvolvimento

- [x] PRD
- [x] Arquitetura
- [x] Banco de Dados
- [x] CRUD de Categorias
- [x] CRUD de Produtos
- [x] Movimentações
- [ ] CRUD de Usuários
- [ ] Autenticação
- [ ] Testes
- [ ] Deploy