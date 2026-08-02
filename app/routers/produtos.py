from fastapi import APIRouter

router = APIRouter()

@router.get('/produtos')
def listar():
    return {'mensagem':'produtos'}
