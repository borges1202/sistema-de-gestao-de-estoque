from sqlite3 import IntegrityError, OperationalError
from fastapi import APIRouter, HTTPException, status
from app.schemas.produto import ProdutoCreate, ProdutoResponse, ProdutoUpdate, ProdutoStatusPatch
from app.database.connection import conectar
from app.repositories.categoria_repository import buscar_categoria
from app.repositories.produto_repository import inserir_produto, buscar_produtos, buscar_produto, modificar_produto, apagar_produto, condicao_produto

router = APIRouter()


@router.post('/produtos', status_code=status.HTTP_201_CREATED)
def criar_produto(produto: ProdutoCreate):
    conexao = None
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        resultado_buscar_categoria = buscar_categoria(
            cursor, produto.categoria_id)

        if resultado_buscar_categoria is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='Categoria não encontrada.'
            )

        inserir_produto(cursor, produto.nome, produto.sku.upper(
        ), produto.descricao, produto.estoque_minimo, produto.categoria_id)

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

        resultados = buscar_produtos(cursor)

        resultados_lista = []
        for resultado in resultados:
            id, nome, sku, descricao, quantidade, estoque_minimo, categoria_id, ativo, criado_em, atualizado_em = resultado
            resultado = {'id': id,
                         'nome': nome,
                         'sku': sku,
                         'descricao': descricao,
                         'quantidade': quantidade,
                         'estoque_minimo': estoque_minimo,
                         'categoria_id': categoria_id,
                         'ativo': ativo,
                         'criado_em': criado_em,
                         'atualizado_em': atualizado_em
                         }
            resultados_lista.append(resultado)

        return resultados_lista

    except OperationalError:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    finally:
        if conexao is not None:
            conexao.close()


@router.get('/produtos/{id}', response_model=ProdutoResponse)
def listar_produto_id(id: int):
    conexao = None
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        resultado = buscar_produto(cursor, id)

        if resultado is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail='Produto não encontrado.')

        id, nome, sku, descricao, quantidade, estoque_minimo, categoria_id, ativo, criado_em, atualizado_em = resultado
        return {'id': id,
                'nome': nome,
                'sku': sku,
                'descricao': descricao,
                'quantidade': quantidade,
                'estoque_minimo': estoque_minimo,
                'categoria_id': categoria_id,
                'ativo': ativo,
                'criado_em': criado_em,
                'atualizado_em': atualizado_em
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

        resultado_busca_categoria = buscar_categoria(
            cursor, produto.categoria_id)

        if resultado_busca_categoria is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='Categoria não encontrada')

        resultado = modificar_produto(cursor, produto.nome, produto.descricao,
                                      produto.estoque_minimo, produto.categoria_id, id)

        if resultado > 0:
            conexao.commit()
            return {'mensagem': 'Produto atualizado com sucesso.'}

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
def deletar_produto(id: int):
    conexao = None
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        resultado = apagar_produto(cursor, id)

        if resultado > 0:
            conexao.commit()
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail='Produto não encontrado.')

    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='Esse produto possui movimentações.'
        )

    except OperationalError:
        if conexao is not None:
            conexao.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    finally:
        if conexao is not None:
            conexao.close()


@router.patch('/produtos/{id}/status')
def status_produto(id: int, produto: ProdutoStatusPatch):
    conexao = None
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        resposta = condicao_produto(cursor, produto.ativo, id)

        if resposta > 0:
            conexao.commit()
            return {'mensagem': f'Produto {"Ativo" if produto.ativo else "Inativo"}'}
        else:
            if conexao is not None:
                conexao.rollback()
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='Produto não encontrado'
            )

    except OperationalError:
        if conexao is not None:
            conexao.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

    finally:
        if conexao is not None:
            conexao.close()
