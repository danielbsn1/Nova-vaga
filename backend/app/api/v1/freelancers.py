from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_freelancers():
    return []

@router.get("/{freelancer_id}")
def get_freelancer(freelancer_id: int):
    return {}
