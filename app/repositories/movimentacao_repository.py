def buscar_produto_movimentacao(cursor, movimentacoes_produto_id):
    cursor.execute(
        """SELECT ativo, quantidade  FROM produtos WHERE id = ?""",
        (movimentacoes_produto_id,),
    )
    return cursor.fetchone()


def buscar_usuario_movimentacao(cursor, movimentacoes_usuario_id):
    cursor.execute(
        """SELECT ativo FROM usuarios WHERE id = ?""", (
            movimentacoes_usuario_id,)
    )
    return cursor.fetchone()


def modificar_produto_movimentacao(cursor, estoque_atual, datetime, movimentacoes):
    cursor.execute(
        """UPDATE produtos SET quantidade = ?, atualizado_em = ? WHERE id = ?""",
        (estoque_atual, datetime, movimentacoes),
    )


def inserir_movimentacao(cursor, movimentacoes_produto_id, movimentacoes_usuario_id, tipo, movimentacoes_quantidade, estoque_anterior, estoque_atual, movimentacoes_observacao):
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
            movimentacoes_produto_id,
            movimentacoes_usuario_id,
            tipo,
            movimentacoes_quantidade,
            estoque_anterior,
            estoque_atual,
            movimentacoes_observacao,
        ),
    )


def buscar_movimentacoes(cursor):
    cursor.execute(
        """SELECT id, produto_id, usuario_id, tipo, quantidade, estoque_anterior, estoque_atual, observacao, criado_em FROM movimentacoes""")

    return cursor.fetchall()


def buscar_movimentacao(cursor, movimentacao_id):
    cursor.execute(
        """SELECT id, produto_id, usuario_id, tipo, quantidade, estoque_anterior, estoque_atual, observacao, criado_em FROM movimentacoes WHERE id = ?""",
        (movimentacao_id,),
    )

    return cursor.fetchone()
