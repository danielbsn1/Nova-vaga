from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_empresas():
    return []

@router.get("/{empresa_id}")
def get_empresa(empresa_id: int):
    return {}
