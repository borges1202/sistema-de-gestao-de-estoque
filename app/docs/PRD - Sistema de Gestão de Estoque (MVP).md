# PRD — Sistema de Gestão de Estoque

**Versão:** MVP (0.2)  
**Autor:** Arthur Borges  
**Status:** Em desenvolvimento

---

# 1. Visão Geral

## Objetivo

Desenvolver um sistema web de gestão de estoque para micro e pequenas empresas, permitindo controlar produtos, categorias e movimentações de estoque de forma simples, segura e confiável.

---

# 2. Problema

Grande parte das pequenas empresas ainda utiliza planilhas ou controles manuais para administrar o estoque.

Isso ocasiona:

- Divergência entre estoque físico e sistema;
- Falta de histórico das alterações;
- Dificuldade em identificar responsáveis pelas movimentações;
- Baixa produtividade;
- Alto índice de erros.

---

# 3. Público-alvo

- Pequenos comércios
- Assistências técnicas
- Empresas familiares
- Microempresas
- Lojas de bairro

---

# 4. Funcionalidades Implementadas

## Categorias

- Cadastro
- Listagem
- Consulta por ID
- Atualização
- Exclusão

## Produtos

- Cadastro
- Listagem
- Consulta por ID
- Atualização
- Exclusão
- SKU único
- Controle de estoque mínimo

## Movimentações

- Registro de entrada
- Registro de saída
- Atualização automática do estoque
- Histórico das movimentações
- Registro do usuário responsável
- Validação de estoque insuficiente

---

# 5. Regras de Negócio

- SKU deve ser único.
- Todo produto pertence a uma categoria existente.
- Todo produto possui estoque mínimo.
- Produtos inativos não podem receber movimentações.
- Nenhuma saída pode deixar o estoque negativo.
- Toda movimentação registra:
  - Produto
  - Usuário
  - Tipo
  - Quantidade
  - Estoque anterior
  - Estoque atual
  - Observação
  - Data e hora

---

# 6. Tecnologias

- Python
- FastAPI
- SQLite
- Pydantic
- Git
- GitHub

---

# 7. Estrutura Atual

- CRUD de Categorias
- CRUD de Produtos
- Controle de Movimentações
- Atualização automática do estoque
- Histórico de movimentações
- Tratamento de exceções
- Response Models
- Validação de dados

---

# 8. Funcionalidades Planejadas

## Próxima versão

- CRUD de usuários
- Soft Delete de produtos
- Soft Delete de categorias

## Futuramente

- Login
- JWT
- Controle de permissões
- Dashboard
- Relatórios
- PostgreSQL
- Docker
- Testes automatizados
- Deploy

---

# 9. Critérios de Sucesso

- CRUD completo de Categorias
- CRUD completo de Produtos
- Registro de Entradas
- Registro de Saídas
- Atualização automática do estoque
- Histórico de movimentações
- Impedimento de estoque negativo
- API documentada via Swagger