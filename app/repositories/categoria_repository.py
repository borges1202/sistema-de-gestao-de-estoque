def inserir_categoria(cursor, categoria_nome, categoria_descricao):
    cursor.execute('''INSERT INTO categorias(nome, descricao) VALUES (?, ?)
        ''', (categoria_nome, categoria_descricao))


def buscar_categorias(cursor):
    cursor.execute(
        '''SELECT id, nome, descricao, ativo, criado_em FROM categorias''')
    return cursor.fetchall()


def buscar_categoria(cursor, categoria_id):
    cursor.execute('''SELECT id, nome, descricao, ativo, criado_em FROM categorias WHERE id = ?
          ''', (categoria_id,))
    return cursor.fetchone()


def modificar_categoria(cursor, categoria_nome, categoria_descricao, categoria_id):
    cursor.execute('''UPDATE categorias SET nome = ?, descricao = ? WHERE id = ?''',
                   (categoria_nome, categoria_descricao, categoria_id))
    return cursor.rowcount


def apagar_categoria(cursor, categoria_id):
    cursor.execute('''DELETE FROM categorias WHERE id = ?''', (categoria_id,))
    return cursor.rowcount