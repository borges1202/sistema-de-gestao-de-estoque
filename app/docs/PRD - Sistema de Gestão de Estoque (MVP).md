# PRD — Sistema de Gestão de Estoque

**Versão:** MVP (0.1)  
**Autor:** Arthur Borges  
**Status:** Em planejamento

---

# 1. Visão Geral

## Objetivo

Desenvolver um sistema web de gestão de estoque voltado para micro e pequenas empresas que precisam controlar seus produtos de maneira simples, intuitiva e confiável.

O foco da primeira versão é resolver o problema principal: registrar produtos e controlar as movimentações de estoque sem depender de planilhas.

---

# 2. Problema

Muitas microempresas utilizam planilhas ou controles manuais para gerenciar o estoque.

Isso gera:

- Erros de preenchimento;
- Divergência entre estoque físico e registrado;
- Falta de histórico;
- Dificuldade para identificar quem realizou alterações;
- Perda de tempo.

Além disso, muitos sistemas existentes são complexos para empresas pequenas.

---

# 3. Público-alvo

- Pequenos comércios
- Lojas de bairro
- Assistências técnicas
- Empresas familiares
- Microempresas

## Perfil

- Pouco conhecimento técnico
- Necessidade de rapidez
- Pouco tempo para treinamento

---

# 4. Objetivos

O sistema deve permitir:

- Cadastrar categorias
- Cadastrar produtos
- Registrar entradas
- Registrar saídas
- Consultar estoque
- Consultar histórico
- Saber quem realizou cada movimentação

---

# 5. Princípios

- Interface simples e intuitiva
- Poucos cliques
- Todas as movimentações registradas
- Nunca permitir estoque negativo
- Priorizar simplicidade e confiabilidade

---

# 6. Escopo do MVP

## Categorias

- Cadastrar
- Editar
- Listar

## Produtos

- Cadastrar
- Editar
- Listar
- Buscar
- Desativar

## Movimentações

- Registrar entrada
- Registrar saída
- Registrar ajuste
- Registrar responsável
- Registrar data e horário
- Impedir estoque negativo

## Histórico

- Listar movimentações
- Filtrar por produto
- Filtrar por período

---

# 7. Fora do Escopo

- Login
- Cadastro de usuários
- Controle de permissões
- Dashboard
- Docker
- PostgreSQL
- API pública
- Código de barras
- QR Code
- Controle financeiro
- Relatórios avançados
- Aplicativo mobile
- Multiempresa

---

# 8. Regras de Negócio

- Nome do produto obrigatório
- SKU único
- Todo produto pertence a uma categoria
- Nenhuma saída pode deixar o estoque negativo
- Toda movimentação registra responsável, data, horário e tipo
- Produtos serão desativados, não excluídos

---

# 9. Requisitos Não Funcionais

- Interface intuitiva
- Código organizado
- API REST com FastAPI
- Banco SQLite
- Estrutura preparada para evoluções

---

# 10. Stack Tecnológica

- Python
- FastAPI
- SQLite
- SQLAlchemy
- Git
- GitHub

---

# 11. Roadmap

## MVP (0.1)

- Sistema funcional

## v0.2

- Login
- Cadastro de usuários

## v0.3

- Permissões
- Dashboard

## v1.0

- PostgreSQL
- Docker
- Testes automatizados
- Deploy

---

# 12. Critérios de Sucesso

- Cadastrar categorias
- Cadastrar produtos
- Registrar entradas
- Registrar saídas
- Impedir estoque negativo
- Consultar histórico
- Identificar o responsável por cada movimentação
- Executar a aplicação localmente