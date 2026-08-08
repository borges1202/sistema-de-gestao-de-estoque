from sqlite3 import IntegrityError, OperationalError
from fastapi import APIRouter, HTTPException, status
from app.schemas.movimentacoes import MovimentacoesCreate, MovimentacoesResponse
from app.database.connection import conectar
from datetime import datetime
from app.repositories.movimentacao_repository import buscar_produto_movimentacao, buscar_usuario_movimentacao, modificar_produto_movimentacao, inserir_movimentacao, buscar_movimentacoes, buscar_movimentacao

router = APIRouter()


@router.post("/movimentacoes", status_code=status.HTTP_201_CREATED)
def criar_movimentacao(movimentacoes: MovimentacoesCreate):
    conexao = None
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        resultado_busca_produto = buscar_produto_movimentacao(
            cursor, movimentacoes.produto_id)

        if resultado_busca_produto is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Produto não encontrado."
            )

        produto_ativo, estoque_anterior = resultado_busca_produto

        if produto_ativo == 0:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT, detail="Produto inativo."
            )

        resultado_busca_usuario = buscar_usuario_movimentacao(
            cursor, movimentacoes.usuario_id)

        if resultado_busca_usuario is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Usuario não encontrado"
            )

        usario_ativo, = resultado_busca_usuario

        if usario_ativo == 0:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail='Usuario inativo.'
            )

        tipo = movimentacoes.tipo

        if tipo == "ENTRADA":
            estoque_atual = estoque_anterior + movimentacoes.quantidade

        elif tipo == "SAIDA":

            if movimentacoes.quantidade > estoque_anterior:
                raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT,
                    detail="Estoque insuficiente para realizar a saída.",
                )

            else:
                estoque_atual = estoque_anterior - movimentacoes.quantidade

        modificar_produto_movimentacao(
            cursor, estoque_atual, datetime.now(), movimentacoes.produto_id)

        inserir_movimentacao(cursor, movimentacoes.produto_id, movimentacoes.usuario_id, tipo,
                             movimentacoes.quantidade, estoque_anterior, estoque_atual, movimentacoes.observacao,)

        conexao.commit()
        return {"mensagem": f"{tipo} Bem sucedida"}

    except IntegrityError:
        if conexao is not None:
            conexao.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Não foi possível registrar a movimentação por conflito de integridade.",
        )

    except OperationalError:
        if conexao is not None:
            conexao.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    finally:
        if conexao is not None:
            conexao.close()


@router.get("/movimentacoes", response_model=list[MovimentacoesResponse])
def listar_movimentacoes():
    conexao = None
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        resultados = buscar_movimentacoes(cursor)

        resultados_lista = []

        for resultado in resultados:
            (
                id,
                produto_id,
                usuario_id,
                tipo,
                quantidade,
                estoque_anterior,
                estoque_atual,
                observacao,
                criado_em,
            ) = resultado

            resultado = {
                "id": id,
                "produto_id": produto_id,
                "usuario_id": usuario_id,
                "tipo": tipo,
                "quantidade": quantidade,
                "estoque_anterior": estoque_anterior,
                "estoque_atual": estoque_atual,
                "observacao": observacao,
                "criado_em": criado_em,
            }
            resultados_lista.append(resultado)

        return resultados_lista

    except OperationalError:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    finally:
        if conexao is not None:
            conexao.close()


@router.get("/movimentacoes/{id}", response_model=MovimentacoesResponse)
def listar_movimentacao_id(id: int):
    conexao = None
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        resultado = buscar_movimentacao(cursor, id)

        if resultado is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Movimentação não encontrada.",
            )

        (
            id,
            produto_id,
            usuario_id,
            tipo,
            quantidade,
            estoque_anterior,
            estoque_atual,
            observacao,
            criado_em,
        ) = resultado
        return {
            "id": id,
            "produto_id": produto_id,
            "usuario_id": usuario_id,
            "tipo": tipo,
            "quantidade": quantidade,
            "estoque_anterior": estoque_anterior,
            "estoque_atual": estoque_atual,
            "observacao": observacao,
            "criado_em": criado_em,
        }

    except OperationalError:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    finally:
        if conexao is not None:
            conexao.close()
