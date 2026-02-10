from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.api.deps import get_current_user
from app.models.vaga import Vaga
from app.models.user import User
from app.schemas.vaga import VagaCreate, VagaResponse

router = APIRouter()

@router.get("/", response_model=list[VagaResponse])
def get_vagas(db: Session = Depends(get_db)):
    return db.query(Vaga).all()

@router.get("/{vaga_id}", response_model=VagaResponse)
def get_vaga(vaga_id: int, db: Session = Depends(get_db)):
    return db.query(Vaga).filter(Vaga.id == vaga_id).first()

@router.post("/", response_model=VagaResponse)
def create_vaga(
    vaga: VagaCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    db_vaga = Vaga(**vaga.dict(), empresa_id=current_user.id)
    db.add(db_vaga)
    db.commit()
    db.refresh(db_vaga)
    return db_vaga
