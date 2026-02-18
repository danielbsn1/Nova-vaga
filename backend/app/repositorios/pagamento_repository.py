from sqlalchemy.orm import Session
from app.models.pagamento import Pagamento

def criar_pagamento(
        db : Session,
        user_id: int,
        plano_id: str,
        stripe_session_id: str,
) -> Pagamento:
    pagamento = Pagamento(
        user_id=user_id,
        plano_id=plano_id,
        stripe_session_id=stripe_session_id,
        status="pendente"
    )
    db.add(pagamento)
    db.commit()
    db.refresh(pagamento)


    return pagamento


def buscar_por_session_id(
    db: Session,
    session_id: str
) -> Pagamento | None:
    return (
        db.query(Pagamento)
        .filter(Pagamento.stripe_session_id == session_id)
        .first()
    )