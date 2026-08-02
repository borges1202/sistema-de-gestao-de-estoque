from fastapi import APIRouter

router = APIRouter()

@router.get('/categorias')
def listar():
    return {'mensagem': 'categorias'}