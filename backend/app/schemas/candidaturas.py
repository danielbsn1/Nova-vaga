from pydantic import BaseModel
from datetime import datetime

class CandidaturaCreate(BaseModel):
    vaga_id: int

class CandidaturaResponse(BaseModel):
    id: int
    vaga_id: int
    user_id: int
    status: str
    created_at: datetime

    class Config:
        from_attributes = True