from fastapi import APIRouter, Depends
from app.api.deps import get_current_user
from app.schemas.pagamento import PagamentoCreate, PagamentoResponse
from app.services.pagamento_service import create_checkout_session

router = APIRouter()

@router.post("/checkout", response_model=PagamentoResponse)
def checkout(
    pagamento: PagamentoCreate,
    current_user = Depends(get_current_user)
):
    return create_checkout_session(pagamento.planoId, current_user.id)
