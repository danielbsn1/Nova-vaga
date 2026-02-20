from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.security import get_current_user, verificar_permissao
from app.models.user import User
from app.models.vaga import Vaga
from app.models.candidatura import Candidatura

router = APIRouter(prefix="/candidaturas", tags=["candidaturas"])


@router.patch("/{vaga_id}/fechar")
def fechar_vaga(
    vaga_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    verificar_permissao(current_user, ["empresa"])

    vaga = db.query(Vaga).filter(Vaga.id == vaga_id).first()

    if not vaga:
        raise HTTPException(status_code=404, detail="Vaga não encontrada")

    if vaga.empresa_id != current_user.id:
        raise HTTPException(status_code=403, detail="Sem permissão")

    try:
        vaga.status = "fechada"
        db.commit()
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=500, 
            detail="Erro ao fechar vaga. Tente novamente."
        )
    
    return {"message": "Vaga fechada com sucesso"}




@router.post("/{vaga_id}")
def candidatar_vaga(
    vaga_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    verificar_permissao(current_user, ["candidato"])


    candidatura_existe = (
        db.query(Candidatura)
        .filter(
            Candidatura.vaga_id == vaga_id,
            Candidatura.candidato_id == current_user.id
        )
        .first()
    )

    if candidatura_existe:
        raise HTTPException(status_code=400, detail="Já se candidatou")

    candidatura = Candidatura(
        vaga_id=vaga_id,
        candidato_id=current_user.id,
        status="em_analise"
    )

    db.add(candidatura)
    
    try:
        db.commit()
        db.refresh(candidatura)
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail="Erro ao realizar candidatura. Tente novamente."
        )

    return {"message": "Candidatura realizada com sucesso"}

def get_vaga_or_404(db: Session, vaga_id: int) -> Vaga:
    vaga = db.query(Vaga).filter(Vaga.id == vaga_id).first()
    if not vaga:
        raise HTTPException(status_code=404, detail="Vaga não encontrada")
    return vaga
