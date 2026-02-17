from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.security import get_current_user
from app.core.security import verificar_permissao
from app.models.user import User
from app.models.vaga import Vaga
from app.models.candidatura import Candidatura
from app.schemas.candidaturas import CandidaturaResponse
from app.models.notificacao import Notificacao
from app.core.notificacao import criar_notificacao
router = APIRouter(prefix="/candidaturas", tags=["candidaturas"])
@router.patch("/{vaga_id}/fechar")
def fechar_vaga(
    vaga_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    #  Só empresa
    verificar_permissao(current_user, ["empresa"])

    vaga = db.query(Vaga).filter(Vaga.id == vaga_id).first()

    if not vaga:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Vaga não encontrada"
        )

    if vaga.empresa_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Você não tem permissão para fechar esta vaga"
        )

    vaga.status = "fechada"
    db.commit()
    return {"message": "Vaga fechada com sucesso"}

@router.post("/{vaga_id}")
def candidatar_vaga(
    vaga_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    verificar_permissao(current_user, ["candidato"])

    vaga = db.query(Vaga).filter(Vaga.id == vaga_id).first()

    if not vaga: 
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Vaga não encontrada"
        )
    
    Candidatura_existe = (
        db.query(Candidatura)
        .filter(
            Candidatura.vaga_id == vaga_id,
            Candidatura.candidato_id == current_user.id
        )
        .first()
    )

    if Candidatura_existe:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Você já se candidatou a esta vaga"
        )
    
    candidatura = Candidatura(
        vaga_id=vaga_id,
        candidato_id=current_user.id,
        status="em_analise"
      )
    db.add(candidatura)
    db.commit()
    db.refresh(candidatura)

    return {"message": "Candidatura realizada com sucesso"}

router = APIRouter(prefix="/vagas", tags=["vagas"])

@router.get("/{vaga_id}/candidaturas")
def listar_candidaturas_vaga(
    vaga_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    verificar_permissao(current_user, ["empresa"])

    vaga = db.query(Vaga).filter(Vaga.id == vaga_id).first()

    if not vaga:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Vaga não encontrada"
        )

    if vaga.empresa_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Você não tem permissão para acessar as candidaturas desta vaga"
        )

    candidaturas = (
        db.query(Candidatura)
        .filter(Candidatura.vaga_id == vaga_id)
        .all()
    )

    return [CandidaturaResponse.from_orm(candidatura) for candidatura in candidaturas]