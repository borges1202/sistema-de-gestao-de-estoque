from sqlite3 import IntegrityError,OperationalError
from fastapi import APIRouter,HTTPException,status
from app.schemas.usuarios import UsuarioCreate, UsuarioResponse, UsuarioStatusPatch, UsuarioUpdate
from app.database.connection import conectar

router = APIRouter()

@router.post('/usuarios', status_code=status.HTTP_201_CREATED)
def criar_usuario(usuarios: UsuarioCreate):
    conexao = None
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        
        cursor.execute('''INSERT INTO usuarios(nome,cpf,telefone)
        VALUES(?,?,?)''', (usuarios.nome, usuarios.cpf, usuarios.telefone))

        conexao.commit()
        return {'mensagem':'Usuario criado com sucesso.'}

    except IntegrityError:
        if conexao is not None:
            conexao.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='Esse cpf já está cadastrado.'
        )

    except OperationalError:
        if conexao is not None:
            conexao.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    finally:
        if conexao is not None:
            conexao.close()



@router.get('/usuarios', response_model=list[UsuarioResponse])
def listar_usuarios():
    conexao = None
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute('''SELECT id, nome, cpf, telefone, ativo, criado_em FROM usuarios''')
        resultados = cursor.fetchall()
        resultados_list = []
        for resultado in resultados:
             id, nome, cpf, telefone, ativo, criado_em = resultado
             resultado = {
                 'id':id,
                 'nome':nome,
                 'cpf':cpf,
                 'telefone':telefone,
                 'ativo':ativo,
                 'criado_em':criado_em
             }
             resultados_list.append(resultado)

        return resultados_list
    except OperationalError:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
    finally:
        if conexao is not None:
            conexao.close()




@router.get('/usuarios/{id}', response_model=UsuarioResponse)
def listar_usuario(id: int):
    conexao = None
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute('''SELECT id, nome, cpf, telefone, ativo, criado_em FROM usuarios WHERE id = ?''', (id,))
        resultado = cursor.fetchone()

        if resultado is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='Usuario não encontrado.'
            )

        id, nome, cpf, telefone, ativo, criado_em = resultado


        return  {
            'id':id,
            'nome':nome,
            'cpf':cpf,
            'telefone':telefone,
            'ativo':ativo,
            'criado_em':criado_em
        }

    except OperationalError:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
    finally:
        if conexao is not None:
            conexao.close()



@router.put('/usuarios/{id}')
def atualizar_usuario(id: int, usuario: UsuarioUpdate):
    conexao = None
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute('''UPDATE usuarios
        SET nome = ?, telefone = ?
        WHERE id = ?''', (usuario.nome, usuario.telefone, id,))

        if cursor.rowcount > 0:
            conexao.commit()
            return {'mensagem':'Usuario atualizado com sucesso.'}
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='usuarios não encontrado.')

    except IntegrityError:
        if conexao is not None:
            conexao.rollback()
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail='Registro duplicado.')

    except OperationalError:

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
    finally:
        if conexao is not None:
            conexao.close()



@router.patch('/usuarios/{id}/status')
def status_usuario(id:int, usuarios:UsuarioStatusPatch):
    conexao = None
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute('''UPDATE usuarios SET ativo = ? WHERE id = ?''', (usuarios.ativo, id,))

        if cursor.rowcount > 0:
            conexao.commit()
            return {'mensagem':f'usuarios {"Ativo" if usuarios.ativo else "Inativo"}'}
        else:
            if conexao is not None:
                conexao.rollback()
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='Usuario não encontrado.'
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
