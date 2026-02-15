from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.security import get_current_user
from app.core.security import verificar_permissao
from app.models.user import User
from app.models.vaga import Vaga
from app.models.candidatura import Candidatura
from app.schemas.candidaturas import CandidaturaResponse
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

