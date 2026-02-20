from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.security import get_current_user, verificar_permissao
from app.models.user import User
from app.models.vaga import Vaga
from app.models.candidatura import Candidatura
from app.schemas.candidaturas import CandidaturaResponse

router = APIRouter(prefix="/vagas", tags=["vagas"])


def get_vaga_or_404(db: Session, vaga_id: int) -> Vaga:
    vaga = db.query(Vaga).filter(Vaga.id == vaga_id).first()
    if not vaga:
        raise HTTPException(status_code=404, detail="Vaga não encontrada")
    return vaga


def verificar_permissao_vaga(vaga: Vaga, user: User):
    if vaga.empresa_id != user.id:
        raise HTTPException(status_code=403, detail="Sem permissão")


@router.get("/{vaga_id}/candidaturas")
def listar_candidaturas_vaga(
    vaga_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    verificar_permissao(current_user, ["empresa"])
    
    vaga = get_vaga_or_404(db, vaga_id)
    verificar_permissao_vaga(vaga, current_user)

    candidaturas = (
        db.query(Candidatura)
        .filter(Candidatura.vaga_id == vaga_id)
        .all()
    )

    return [CandidaturaResponse.from_orm(c) for c in candidaturas]