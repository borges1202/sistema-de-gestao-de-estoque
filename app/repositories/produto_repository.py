def inserir_produto(cursor, produto_nome, produto_sku, produto_descricao, produto_estoque_minimo, produto_categoria_id):
    cursor.execute('''INSERT INTO produtos(nome, sku, descricao, estoque_minimo, categoria_id) VALUES (?, ?, ?, ?, ?)
            ''', (produto_nome, produto_sku.upper(), produto_descricao, produto_estoque_minimo, produto_categoria_id))


def buscar_produtos(cursor):
    cursor.execute(
        '''SELECT id, nome, sku, descricao, quantidade, estoque_minimo, categoria_id, ativo, criado_em, atualizado_em FROM produtos''')
    return cursor.fetchall()


def buscar_produto(cursor, produto_id):
    cursor.execute('''SELECT id, nome, sku, descricao, quantidade, estoque_minimo, categoria_id, ativo, criado_em, atualizado_em FROM produtos
          WHERE id = ?
          ''', (produto_id,))
    return cursor.fetchone()


def modificar_produto(cursor, produto_nome, produto_descricao, produto_estoque_minimo, produto_categoria_id, produto_id):
    cursor.execute('''UPDATE produtos
        SET nome = ?, descricao = ?, estoque_minimo = ?, categoria_id = ?
        WHERE id = ?''', (produto_nome, produto_descricao, produto_estoque_minimo, produto_categoria_id, produto_id))
    return cursor.rowcount


def apagar_produto(cursor, produto_id):
    cursor.execute('''DELETE FROM produtos WHERE id = ?
        ''', (produto_id,))
    return cursor.rowcount


def condicao_produto(cursor, produto_ativo, produto_id):
    cursor.execute('''UPDATE produtos SET ativo = ? WHERE id = ?''',
                   (produto_ativo, produto_id))
    return cursor.rowcount
