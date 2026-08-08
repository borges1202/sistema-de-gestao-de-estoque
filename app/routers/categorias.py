from sqlite3 import IntegrityError, OperationalError
from fastapi import APIRouter, HTTPException, status
from app.schemas.categoria import CategoriaValidation, CategoriaResponse
from app.database.connection import conectar
from app.repositories.categoria_repository import inserir_categoria, buscar_categorias, buscar_categoria, modificar_categoria, apagar_categoria


router = APIRouter()


@router.post('/categorias', status_code=status.HTTP_201_CREATED)
def criar_categoria(categoria: CategoriaValidation):
    conexao = None
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        inserir_categoria(cursor, categoria.nome, categoria.descricao)

        conexao.commit()
        return {'mensagem': 'Categoria criada com sucesso.'}

    except IntegrityError:
        if conexao is not None:
            conexao.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='Essa categoria já existe.')

    except OperationalError:
        if conexao is not None:
            conexao.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    finally:
        if conexao is not None:
            conexao.close()


@router.get('/categorias', response_model=list[CategoriaResponse])
def listar_categorias():
    conexao = None
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        resultados = buscar_categorias(cursor)

        resultados_lista = []
        for resultado in resultados:
            id, nome, descricao, ativo, criado_em = resultado
            resultado = {'id': id,
                         'nome': nome,
                         'descricao': descricao,
                         'ativo': ativo,
                         'criado_em': criado_em}
            resultados_lista.append(resultado)

        return resultados_lista
    except OperationalError:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    finally:
        if conexao is not None:
            conexao.close()


@router.get('/categorias/{id}', response_model=CategoriaResponse)
def listar_categoria_id(id: int):
    conexao = None
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        resultado = buscar_categoria(cursor, id)

        if resultado is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail='Categoria não encontrada.')

        id, nome, descricao, ativo, criado_em = resultado
        return {'id': id,
                'nome': nome,
                'descricao': descricao,
                'ativo': ativo,
                'criado_em': criado_em}

    except OperationalError:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    finally:
        if conexao is not None:
            conexao.close()


@router.put('/categorias/{id}')
def atualizar_categoria(id: int, categoria: CategoriaValidation):
    conexao = None
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        resultado = modificar_categoria(
            cursor, categoria.nome, categoria.descricao, id)

        if resultado > 0:
            conexao.commit()
            return {'mensagem': 'Categoria atualizada com sucesso.'}

        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail='Categoria não encontrada.')

    except IntegrityError:
        if conexao is not None:
            conexao.rollback()
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail='Registro duplicado.')

    except OperationalError:
        if conexao is not None:
            conexao.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    finally:
        if conexao is not None:
            conexao.close()


@router.delete('/categorias/{id}', status_code=204)
def deletar_categoria(id: int):
    conexao = None
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        resultado = apagar_categoria(cursor, id)

        if resultado > 0:
            conexao.commit()
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail='Categoria não encontrada.')

    except IntegrityError:
        if conexao is not None:
            conexao.rollback()
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail='Essa categoria possui produtos vinculados.')

    except OperationalError:
        if conexao is not None:
            conexao.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    finally:
        if conexao is not None:
            conexao.close()
