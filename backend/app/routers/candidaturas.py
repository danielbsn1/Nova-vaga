from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import get_current_user
from app.core.security import verificar_permissao

from app.models.user import User
from app.models.vaga import Vaga
from app.models.candidatura import Candidatura

from app.schemas.candidaturas import (
    CandidaturaCreate,
    CandidaturaResponse
)

from app.core.notificacao import criar_notificacao


router = APIRouter(prefix="/candidaturas", tags=["candidaturas"])



# LISTAR CANDIDATURAS

@router.get("/", response_model=list[CandidaturaResponse])
def listar_candidaturas(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # Freelancer vê apenas as próprias candidaturas
    if current_user.tipo == "freelancer":
        return db.query(Candidatura).filter(
            Candidatura.freelancer_id == current_user.id
        ).all()

    # Empresa vê candidaturas das suas vagas
    if current_user.tipo == "empresa":
        return (
            db.query(Candidatura)
            .join(Vaga)
            .filter(Vaga.empresa_id == current_user.id)
            .all()
        )

    return []



# CANDIDATAR-SE A UMA VAGA

@router.post("/")
def candidatar_vaga(
    data: CandidaturaCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # Apenas freelancer pode se candidatar
    verificar_permissao(current_user, ["freelancer"])

    # Buscar vaga
    vaga = db.query(Vaga).filter(
        Vaga.id == data.vaga_id
    ).first()

    if not vaga:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Vaga não encontrada"
        )

    # Bloquear candidatura em vaga fechada
    if vaga.status == "fechada":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Esta vaga já está fechada"
        )

    # Verificar se já se candidatou
    candidatura_existente = db.query(Candidatura).filter(
        Candidatura.vaga_id == vaga.id,
        Candidatura.freelancer_id == current_user.id
    ).first()

    if candidatura_existente:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Você já se candidatou para esta vaga"
        )

    # Criar candidatura
    candidatura = Candidatura(
        vaga_id=vaga.id,
        freelancer_id=current_user.id
    )

    db.add(candidatura)
    db.commit()
    db.refresh(candidatura)

    return {"message": "Candidatura realizada com sucesso"}



# APROVAR CANDIDATURA
@router.patch("/{candidatura_id}/aprovar")
def aprovar_candidatura(
    candidatura_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # Apenas empresa
    verificar_permissao(current_user, ["empresa"])

    candidatura = db.query(Candidatura).filter(
        Candidatura.id == candidatura_id
    ).first()

    if not candidatura:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Candidatura não encontrada"
        )

    vaga = db.query(Vaga).filter(
        Vaga.id == candidatura.vaga_id
    ).first()

    if vaga.empresa_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Você não pode aprovar esta candidatura"
        )

    # Contar candidaturas aceitas
    total_aceitas = db.query(Candidatura).filter(
        Candidatura.vaga_id == vaga.id,
        Candidatura.status == "aceita"
    ).count()

    if total_aceitas >= vaga.quantidade_vagas:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Limite de vagas já preenchido"
        )

    # Aprovar candidatura
    candidatura.status = "aceita"

    # Fechar vaga se atingir limite
    if total_aceitas + 1 == vaga.quantidade_vagas:
        vaga.status = "fechada"

    # Notificação
    criar_notificacao(
        db=db,
        user_id=candidatura.freelancer_id,
        mensagem="Sua candidatura foi aceita 🎉"
    )

    db.commit()

    return {
        "message": "Candidatura aprovada com sucesso",
        "vaga_status": vaga.status
    }



# RECUSAR CANDIDATURA

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

    vaga = db.query(Vaga).filter(
        Vaga.id == candidatura.vaga_id
    ).first()

    if vaga.empresa_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Você não pode gerenciar esta candidatura"
        )

    candidatura.status = "recusada"

    criar_notificacao(
        db=db,
        user_id=candidatura.freelancer_id,
        mensagem="Sua candidatura foi recusada 😕"
    )

    db.commit()

    return {"message": "Candidatura recusada com sucesso"}