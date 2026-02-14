from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

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