from fastapi import APIRouter
from app.schemas.categoria import CategoriaCreate
from app.database.connection import conectar

router = APIRouter()

@router.post('/categorias', status_code=201)
def criar_categoria(categoria: CategoriaCreate):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute('''INSERT INTO categorias(
        nome,
        descricao
    )
    VALUES (?, ?)
    ''',(categoria.nome, categoria.descricao))

    conexao.commit()
    conexao.close()

    return {'Mensagem':'Categoria Criada com sucesso!'}

@router.get('/categorias')
def listar_categorias():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute('''SELECT * FROM categorias''')

    resultado = cursor.fetchall()
    conexao.close()
    return resultado

@router.put('/categorias/{id}')
def atualizar_categoria(id: int, categoria: CategoriaCreate):
    conexao = conectar()
    cursor = conexao.cursor()


    sql = '''UPDATE categorias
    SET nome = ?, descricao = ?
    WHERE id = ?'''
    valor = (categoria.nome, categoria.descricao, id)

    cursor.execute(sql,valor)

    if cursor.rowcount > 0:
        conexao.commit()
        conexao.close()

        return {'Mensagem':'Update Bem-Sucessido'}
    else:
        conexao.close()
        return {'Mensagem':'Categoria não encontrada'}

@router.delete('/categorias/{id}')
def deletar_categoria(id:int):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute('''DELETE FROM categorias
    WHERE id = ?
    ''', (id,))

    if cursor.rowcount > 0:
        conexao.commit()
        conexao.close()

        return {'Mensagem':'Delete Bem-Sucessido'}
    else:
        conexao.close()
        return {'Mensagem':'Categorina não encontrada'}