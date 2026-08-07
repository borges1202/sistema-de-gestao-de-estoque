def insert_usuario(cursor, usuario_nome, usuario_cpf, usuario_telefone):
        cursor.execute('''INSERT INTO usuarios(nome,cpf,telefone)
        VALUES(?,?,?)''', (usuario_nome, usuario_cpf, usuario_telefone))

def get_usuarios(cursor):
        cursor.execute('''SELECT id, nome, cpf, telefone, ativo, criado_em FROM usuarios''')
        return cursor.fetchall()

def get_usuario(cursor, usuario_id:int):
        cursor.execute('''SELECT id, nome, cpf, telefone, ativo, criado_em FROM usuarios WHERE id = ?''', (usuario_id,))
        return cursor.fetchone()

def put_usuario(cursor, usuario_nome, usuario_telefone, usuario_id:int):
        cursor.execute('''UPDATE usuarios
        SET nome = ?, telefone = ?
        WHERE id = ?''', (usuario_nome, usuario_telefone, usuario_id,))
        return cursor.rowcount

def patch_usuario(cursor, usuario_ativo, usuario_id:int):
        cursor.execute('''UPDATE usuarios SET ativo = ? WHERE id = ?''', (usuario_ativo, usuario_id,))
        return cursor.rowcount