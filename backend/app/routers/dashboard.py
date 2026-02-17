from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from sqlalchemy import func

from app.core.security import get_current_user
from app.core.security import verificar_permissao
from app.models.user import User
from app.models.vaga import Vaga
from app.models.candidatura import Candidatura
from app.schemas.candidaturas import CandidaturaResponse
from app.schemas.dashbord import VagaDashboard
from app.schemas.candidaturas import CandidaturaCreate

router = APIRouter(prefix="/dashboard", tags=["dashboard"])

@router.post("/")

def candidatar_vaga(
    data: CandidaturaCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    #  Só freelancer pode se candidatar
    verificar_permissao(current_user, ["freelancer"])

    #  Buscar a vaga
    vaga = db.query(Vaga).filter(
        Vaga.id == data.vaga_id
    ).first()

    if not vaga:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Vaga não encontrada"
        )

    #  BLOQUEIO: vaga fechada
    if vaga.status == "fechada":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Esta vaga já está fechada"
        )

    #  Verificar se já se candidatou
    candidatura_existente = db.query(Candidatura).filter(
        Candidatura.vaga_id == vaga.id,
        Candidatura.freelancer_id == current_user.id
    ).first()

    if candidatura_existente:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Você já se candidatou para esta vaga"
        )

    #  Criar candidatura
    candidatura = Candidatura(
        vaga_id=vaga.id,
        freelancer_id=current_user.id
    )

    db.add(candidatura)
    db.commit()
    db.refresh(candidatura)

    return {"message": "Candidatura realizada com sucesso"}