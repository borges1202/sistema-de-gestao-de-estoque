from sqlite3 import IntegrityError,OperationalError
from fastapi import APIRouter,HTTPException,status
from app.schemas.produto import ProdutoCreate, ProdutoResponse, ProdutoUpdate
from app.database.connection import conectar

router = APIRouter()

@router.post('/produtos', status_code=status.HTTP_201_CREATED)
def criar_produto(produto: ProdutoCreate):
    conexao = None
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute('''SELECT id FROM categorias WHERE id = ?''', (produto.categoria_id,) )
        resultado = cursor.fetchone()

        if resultado is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='Categoria não encontrada.'
            )
        
        cursor.execute('''INSERT INTO produtos(
                nome,
                sku,
                descricao,
                estoque_minimo,
                categoria_id
            )
            VALUES (?, ?, ?, ?, ?)
            ''',(produto.nome, produto.sku.upper(), produto.descricao, produto.estoque_minimo, produto.categoria_id))

        conexao.commit()
        return {'mensagem': 'Produto criado com sucesso.'}
        
    except IntegrityError:
        if conexao is not None:
            conexao.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='Já existe um produto cadastrado com esse SKU.')

    except OperationalError:
        if conexao is not None:
            conexao.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    finally:
        if conexao is not None:
            conexao.close()



@router.get('/produtos', response_model=list[ProdutoResponse])
def listar_produtos():
    conexao = None
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute('''SELECT 
        id, nome, sku, descricao, quantidade, estoque_minimo, categoria_id, ativo, criado_em, atualizado_em FROM produtos''')

        resultados = cursor.fetchall()
        resultados_lista = []
        for resultado in resultados:
            id, nome, sku, descricao, quantidade, estoque_minimo, categoria_id, ativo, criado_em, atualizado_em = resultado
            resultado = {'id':id,
                         'nome':nome,
                         'sku':sku,
                         'descricao':descricao,
                         'quantidade':quantidade,
                         'estoque_minimo':estoque_minimo,
                         'categoria_id':categoria_id,
                         'ativo':ativo,
                         'criado_em':criado_em,
                         'atualizado_em':atualizado_em
                         }
            resultados_lista.append(resultado)
            
        return resultados_lista
    
    except OperationalError:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    finally:
        if conexao is not None:
            conexao.close()



@router.get('/produtos/{id}', response_model=ProdutoResponse)
def listar_produto_id(id:int):
    conexao = None
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute('''SELECT id, nome, sku, descricao, quantidade, estoque_minimo, categoria_id, ativo, criado_em, atualizado_em FROM produtos
          WHERE id = ?
          ''',(id,))
        
        resultado = cursor.fetchone()
        if resultado is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail='Produto não encontrada.')
        
        id, nome, sku, descricao, quantidade, estoque_minimo, categoria_id, ativo, criado_em, atualizado_em = resultado
        return {'id':id,
                         'nome':nome,
                         'sku':sku,
                         'descricao':descricao,
                         'quantidade':quantidade,
                         'estoque_minimo':estoque_minimo,
                         'categoria_id':categoria_id,
                         'ativo':ativo,
                         'criado_em':criado_em,
                         'atualizado_em':atualizado_em
                         }
    
    except OperationalError:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    finally:
        if conexao is not None:
            conexao.close()



@router.put('/produtos/{id}')
def atualizar_produto(id: int, produto: ProdutoUpdate):
    conexao = None
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute('''SELECT id FROM categorias WHERE id = ?''', (produto.categoria_id,))
        resultado = cursor.fetchone()
        if resultado is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='Categoria não encontrada')
        
        sql = '''UPDATE produtos
        SET nome = ?, descricao = ?, estoque_minimo = ?, categoria_id = ?
        WHERE id = ?'''

        valores = (produto.nome, produto.descricao, produto.estoque_minimo, produto.categoria_id, id)
        cursor.execute(sql,valores)

        if cursor.rowcount > 0:
            conexao.commit()
            return {'mensagem':'Produto atualizado com sucesso.'}
        
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='Produto não encontrado.')

    except OperationalError:
        if conexao is not None:
            conexao.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    finally:
        if conexao is not None:
            conexao.close() 



@router.delete('/produtos/{id}', status_code=204)
def deletar_produto(id:int):
    conexao = None
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute('''DELETE FROM produtos
        WHERE id = ?
        ''', (id,))

        if cursor.rowcount > 0:
            conexao.commit()
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail='Produto não encontrado.')
        
    except OperationalError:
        if conexao is not None:
            conexao.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    finally:
        if conexao is not None:
            conexao.close()