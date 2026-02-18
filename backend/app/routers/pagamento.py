from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import get_current_user, verificar_permissao
from app.models.user import User
from app.services.pagamento_service import create_checkout_session
from app.schemas.pagamento import PagamentoCreate, PagamentoResponse


router = APIRouter(prefix="/pagamento", tags=["pagamento"])


@router.post(
    "/checkout",
    response_model=PagamentoResponse
)
def criar_checkout(
    data: PagamentoCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    #  Somente empresa pode pagar
    verificar_permissao(current_user, ["empresa"])

    try:
        checkout = create_checkout_session(
            plano_id=data.plano_id,
            user_id=current_user.id
        )
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Erro ao criar sessão de pagamento"
        )

    return checkout