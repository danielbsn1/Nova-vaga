from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

from app.core.database import get_db
from app.core.security import verify_password, create_access_token
from app.models.empresa import Company


auth_router = APIRouter(prefix="/auth", tags=["Auth"])

@auth_router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    company = db.query(Company).filter(
        Company.email == form_data.username
    ).first()

    if not company or not verify_password(form_data.password, company.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
        )

    access_token = create_access_token(
        data={"sub": str(company.id), "type": "company"}
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }

@auth_router.post("/login/freelancer")

def login_freelancer(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    freelancer = db.query(freelancer).filter(
        freelancer.email == form_data.username
    ).first()

    if not freelancer or not verify_password(form_data.password, freelancer.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
        )

    access_token = create_access_token(
        data={"sub": str(freelancer.id), "type": "freelancer"}
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }
