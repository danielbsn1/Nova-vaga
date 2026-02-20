from sqlalchemy.orm import Session
from app.models.notificacao import Notificacao

def criar_notificacao(
    db: Session,
    user_id: int,
    mensagem: str
):
    notificacao = Notificacao(
        user_id=user_id,
        mensagem=mensagem
    )

    db.add(notificacao)
    db.commit()

    return notificacao
