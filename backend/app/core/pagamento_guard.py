from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.models.pagamento import Pagamento, PagamentoStatus


def empresa_tem_pagamento_pago(db: Session, user_id: int) -> None:
    pagamento = (
        db.query(Pagamento)
        .filter(
            Pagamento.user_id == user_id,
            Pagamento.status == PagamentoStatus.pago
        )
        .order_by(Pagamento.created_at.desc())
        .first()
    )

    if not pagamento:
        raise HTTPException(
            status_code=status.HTTP_402_PAYMENT_REQUIRED,
            detail="Pagamento necessário para criar vagas"
        )