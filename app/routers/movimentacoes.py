from sqlite3 import IntegrityError, OperationalError
from fastapi import APIRouter, HTTPException, status
from app.schemas.movimentacoes import MovimentacoesCreate, MovimentacoesResponse
from app.database.connection import conectar

router = APIRouter()


@router.post("/movimentacoes", status_code=status.HTTP_201_CREATED)
def criar_movimentacao(movimentacoes: MovimentacoesCreate):
    conexao = None
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute(
            """SELECT ativo, quantidade  FROM produtos WHERE id = ?""",
            (movimentacoes.produto_id,),
        )
        resultado_produtos = cursor.fetchone()

        if resultado_produtos is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Produto não encontrado."
            )

        ativo, estoque_anterior = resultado_produtos

        if ativo is False:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT, detail="Produto inativo."
            )

        cursor.execute(
            """SELECT id FROM usuarios WHERE id = ?""", (movimentacoes.usuario_id,)
        )
        resultado_usuario = cursor.fetchone()
        if resultado_usuario is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Usuario não encontrado"
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

        cursor.execute(
            """UPDATE produtos SET quantidade = ? WHERE id = ?""",
            (estoque_atual, movimentacoes.produto_id),
        )

        cursor.execute(
            """INSERT INTO movimentacoes(
            produto_id,
            usuario_id,
            tipo,
            quantidade,
            estoque_anterior,
            estoque_atual,
            observacao
            ) 
            VALUES(?, ?, ?, ?, ?, ?, ?)
            """,
            (
                movimentacoes.produto_id,
                movimentacoes.usuario_id,
                tipo,
                movimentacoes.quantidade,
                estoque_anterior,
                estoque_atual,
                movimentacoes.observacao,
            ),
        )

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

        cursor.execute("""SELECT 
                       id, produto_id, usuario_id, tipo, quantidade, estoque_anterior, estoque_atual, observacao, criado_em
                       FROM movimentacoes""")

        resultados = cursor.fetchall()
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

        cursor.execute(
            """SELECT 
                       id, produto_id, usuario_id, tipo, quantidade, estoque_anterior, estoque_atual, observacao, criado_em
                       FROM movimentacoes
          WHERE id = ?
          """,
            (id,),
        )

        resultado = cursor.fetchone()
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
