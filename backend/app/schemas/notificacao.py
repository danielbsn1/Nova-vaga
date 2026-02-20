from pydantic import BaseModel
from datetime import datetime

class NotificacaoResponse(BaseModel):
    id: int
    mensagem: str
    enum: str
    created_at: datetime

    class Config:
        from_attributes = True