from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import verify_password, create_access_token, get_password_hash
from app.models.user import User
from app.schemas import RegisterSchema, LoginSchema, Token
from typing import List
from app.schemas.vaga import VagaCreate, VagaResponse
from app.models.vaga import Vaga
from app.core.security import get_current_user, verificar_permissao





auth_router = APIRouter(prefix="/auth", tags=["Auth"])

# Endpoint para login   
@auth_router.post("/login", response_model=Token)
def login(data: LoginSchema, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == data.email).first()

    if not db_user or not verify_password(data.password, db_user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciais inválidas",
        )

    token = create_access_token(
        data={"sub": str(db_user.id), "tipo": db_user.tipo}
    )

    return {
        "access_token": token,
        "token_type": "bearer",
    }

# Endpoint para registro
@auth_router.post("/register", response_model=Token)
def register(data: RegisterSchema, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == data.email).first()

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email já registrado",
        )

    new_user = User(
        email=data.email,
        hashed_password=get_password_hash(data.password),
        tipo=data.tipo,
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    token = create_access_token(
        data={"sub": str(new_user.id), "tipo": new_user.tipo}
    )

    return {
        "access_token": token,
        "token_type": "bearer",
    }
# Endpoint para criar vaga (apenas para empresas)
@auth_router.post("/vagas", response_model=VagaResponse)
def criar_vaga(
    vaga: VagaCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    verificar_permissao(current_user, ["empresa"])
    nova_vaga = Vaga(
         titulo=vaga.titulo,
         descricao=vaga.descricao,
         valor = vaga.valor,
         empresa_id=current_user.id
    )
    db.add(nova_vaga)
    db.commit()
    db.refresh(nova_vaga)

    return nova_vaga

