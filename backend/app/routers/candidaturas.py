from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status

from app.core.database import get_db
from app.core.security import get_current_user
from app.core.security import verificar_permissao
from app.models.user import User
from app.models.vaga import Vaga
from app.models.candidatura import Candidatura
from app.schemas.candidaturas import CandidaturaResponse

router = APIRouter(prefix="/candidaturas", tags=["candidaturas"])


@router.get("/", response_model=list[CandidaturaResponse])
def listar_candidaturas(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # FREELANCER → vê só as próprias
    if current_user.tipo == "freelancer":
        return db.query(Candidatura).filter(
            Candidatura.freelancer_id == current_user.id
        ).all()

    # EMPRESA → vê candidaturas das suas vagas
    if current_user.tipo == "empresa":
        return (
            db.query(Candidatura)
            .join(Vaga)
            .filter(Vaga.empresa_id == current_user.id)
            .all()
        )

    return []

@router.patch("/{candidatura_id}/aceitar")
def aceitar_candidatura(
    candidatura_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    #  Só empresa
    verificar_permissao(current_user, ["empresa"])

    candidatura = db.query(Candidatura).filter(
        Candidatura.id == candidatura_id
    ).first()

    if not candidatura:
        raise HTTPException (
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Candidatura não encontrada"
        )

    #  Verificar se a vaga pertence à empresa
    vaga = db.query(Vaga).filter(Vaga.id == candidatura.vaga_id).first()

    if vaga.empresa_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Você não pode gerenciar esta candidatura"
        )
    candidatura.status = "aceita"
    db.commit()

    return {"message": "Candidatura aceita com sucesso"}


@router.patch("/{candidatura_id}/recusar")
def recusar_candidatura(
    candidatura_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    verificar_permissao(current_user, ["empresa"])

    candidatura = db.query(Candidatura).filter(
        Candidatura.id == candidatura_id
    ).first()

    if not candidatura:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Candidatura não encontrada"

        )

    vaga = db.query(Vaga).filter(Vaga.id == candidatura.vaga_id).first()

    if vaga.empresa_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Você não pode gerenciar esta candidatura"
        )

    candidatura.status = "recusada"
    db.commit()

    return {"message": "Candidatura recusada"}


