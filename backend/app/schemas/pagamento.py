from pydantic import BaseModel

class PagamentoCreate(BaseModel):
    plano_id: str

class PagamentoResponse(BaseModel):
    checkout_url: str
    session_id: str
