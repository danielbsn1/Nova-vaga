from pydantic import BaseModel

class PagamentoCreate(BaseModel):
    planoId: str

class PagamentoResponse(BaseModel):
    checkout_url: str
    session_id: str
