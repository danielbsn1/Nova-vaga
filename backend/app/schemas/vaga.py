from pydantic import BaseModel
from datetime import datetime

class VagaBase(BaseModel):
    titulo: str
    descricao: str | None = None
    valor: float

class VagaCreate(VagaBase):
    pass

class VagaResponse(VagaBase):
    id: int
    empresa_id: int
    status: str
    created_at: datetime

    class Config:
        from_attributes = True
