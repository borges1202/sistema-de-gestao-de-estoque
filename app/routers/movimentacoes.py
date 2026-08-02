from fastapi import APIRouter

router = APIRouter()

@router.get('/movimentacoes')
def lista():
    return {'mensagem':'movimentacoes'}