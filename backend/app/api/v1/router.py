from fastapi import APIRouter
from app.api.v1 import auth, empresas, freelancers, vagas, pagamentos

router = APIRouter()

router.include_router(auth.router, prefix="/auth", tags=["auth"])
router.include_router(empresas.router, prefix="/empresas", tags=["empresas"])
router.include_router(freelancers.router, prefix="/freelancers", tags=["freelancers"])
router.include_router(vagas.router, prefix="/vagas", tags=["vagas"])
router.include_router(pagamentos.router, prefix="/pagamentos", tags=["pagamentos"])
