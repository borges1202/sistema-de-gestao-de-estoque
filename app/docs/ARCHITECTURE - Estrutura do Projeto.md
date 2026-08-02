# Arquitetura do Projeto

## Estrutura de Pastas

```text
estoque/
│
├── app/
│   │
│   ├── main.py
│   │   Responsável por iniciar a aplicação FastAPI.
│   │
│   ├── database.py
│   │   Configuração da conexão com o banco SQLite.
│   │
│   ├── models.py
│   │   Modelos (tabelas) do banco de dados.
│   │
│   ├── schemas.py
│   │   Validação dos dados de entrada e saída.
│   │
│   ├── crud.py
│   │   Operações de Create, Read, Update e Delete.
│   │
│   └── routers/
│       │
│       ├── categorias.py
│       │   Rotas relacionadas às categorias.
│       │
│       ├── produtos.py
│       │   Rotas relacionadas aos produtos.
│       │
│       └── movimentacoes.py
│           Rotas relacionadas às movimentações.
│
├── docs/
│   │
│   ├── PRD.md
│   ├── ARCHITECTURE.md
│   └── DATABASE.md
│
├── tests/
│   Testes do projeto.
│
├── requirements.txt
│   Dependências do projeto.
│
├── README.md
│   Documentação principal.
│
└── .gitignore
    Arquivos ignorados pelo Git.
```

---

## Arquitetura

```text
Cliente
   ↓
Rotas (FastAPI)
   ↓
Schemas (Validação)
   ↓
CRUD
   ↓
SQLite
```

---

## Módulos

### Categorias

- Cadastro
- Edição
- Listagem

### Produtos

- Cadastro
- Edição
- Busca
- Desativação

### Movimentações

- Entrada
- Saída
- Ajuste
- Histórico

---

## Ordem de Desenvolvimento

1. PRD
2. ARCHITECTURE.md
3. DATABASE.md
4. Estrutura do projeto
5. Banco de dados
6. Rotas
7. Funcionalidades
8. Testes
9. README
10. Publicação