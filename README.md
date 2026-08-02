# Sistema de Gestão de Estoque

Sistema de gestão de estoque desenvolvido com **Python**, **FastAPI** e **SQLite**, voltado para microempresas que precisam controlar produtos, entradas e saídas de maneira simples e organizada.

O objetivo é substituir planilhas e sistemas excessivamente complexos por uma solução intuitiva, confiável e de fácil utilização.

> **Status:** Em desenvolvimento

---

## Objetivo

Este projeto foi criado para resolver problemas comuns encontrados no controle de estoque de pequenas empresas, como:

- Falta de controle sobre entradas e saídas de produtos;
- Dificuldade em identificar quem realizou uma movimentação;
- Dependência de planilhas;
- Sistemas com excesso de funcionalidades para operações simples.

A proposta é desenvolver uma API REST que sirva como base para um sistema de gestão de estoque simples, escalável e de fácil manutenção.

---

## Tecnologias

- Python
- FastAPI
- SQLite
- Uvicorn

---

## Estrutura do Projeto

```text
app/
│
├── database/
│   ├── connection.py
│
├── docs/
│   ├── PRD - Sistema de Gestão de Estoque (MVP).md
│   └── ARCHITECTURE - Estrutura do Projeto.md
│
├── routers/
│   ├── categorias.py
│   ├── produtos.py
│   └── movimentacoes.py
│
├── main.py
└── __init__.py
```

---

## Banco de Dados

O projeto utiliza SQLite como banco de dados.

A modelagem inicial é composta pelas seguintes entidades:

- Usuários
- Categorias
- Produtos
- Movimentações

---

## Roadmap

### Planejamento

- [x] Definição do PRD
- [x] Arquitetura do projeto
- [x] Modelagem do banco de dados

### Backend

- [x] Configuração do FastAPI
- [x] CRUD de Categorias
- [ ] CRUD de Produtos
- [ ] CRUD de Movimentações
- [ ] Implementação das regras de negócio

### Funcionalidades

- [ ] Controle de estoque
- [ ] Registro de entradas
- [ ] Registro de saídas
- [ ] Histórico de movimentações
- [ ] Dashboard

---

## Como executar

Clone o repositório:

```bash
git clone https://github.com/borges1202/sistema-de-gestao-de-estoque.git
```

Entre na pasta do projeto:

```bash
cd sistema-de-gestao-de-estoque
```

Crie um ambiente virtual:

```bash
python -m venv .venv
```

Ative o ambiente virtual.

### Windows

```bash
.venv\Scripts\activate
```

### Linux/macOS

```bash
source .venv/bin/activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute a aplicação:

```bash
python -m uvicorn app.main:app --reload
```

A documentação interativa estará disponível em:

```text
http://127.0.0.1:8000/docs
```

---

## Próximos Passos

Os próximos objetivos do projeto são:

- Implementar o CRUD de Categorias;
- Desenvolver o CRUD de Produtos;
- Implementar as movimentações de estoque;
- Automatizar a criação do banco de dados;
- Desenvolver uma interface web para o sistema.

---

## Autor

**Arthur Borges**

GitHub: https://github.com/borges1202

LinkedIn: https://www.linkedin.com/in/borgess/