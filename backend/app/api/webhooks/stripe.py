import stripe
from fastapi import APIRouter, Request, HTTPException, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.config import settings
from app.models.pagamento import Pagamento
from app.models.user import User
from app.schemas.pagamento import PagamentoCreate, PagamentoResponse
from app.repositorios.pagamento_repository import buscar_por_session_id
from app.services.pagamento_service import create_checkout_session
from app.services.pagamento_service import create_checkout_session

stripe.api_key = settings.STRIPE_SECRET_KEY

router = APIRouter(prefix="/webhooks", tags=["webhooks"])


@router.post("/stripe")
async def stripe_webhook(
    request: Request,
    db: Session = Depends(get_db)
):
    payload = await request.body()
    sig_header = request.headers.get("stripe-signature")

    try:
        event = stripe.Webhook.construct_event(
            payload,
            sig_header,
            settings.STRIPE_WEBHOOK_SECRET
        )
    except stripe.error.SignatureVerificationError:
        raise HTTPException(status_code=400, detail="Invalid signature")

    #  Evento correto
    if event["type"] == "checkout.session.completed":
     session_stripe = event["data"]["object"]
    session_id = session_stripe["id"]
    stripe_session = stripe.checkout.Session.retrieve(session_id)

    pagamento = (
        db.query(Pagamento)
        .filter(Pagamento.stripe_session_id == session_id)
        .first()
    )

    if not pagamento:
        raise HTTPException(status_code=404, detail="Pagamento não encontrado")

    
    if pagamento.status == "pago":
        return {"status": "already_processed"}

    pagamento.status = "pago"

    user = db.query(User).filter(User.id == pagamento.user_id).first()
    if user:
        user.is_active = True

    db.commit()
