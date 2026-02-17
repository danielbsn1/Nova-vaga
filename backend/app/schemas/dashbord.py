from pydantic import BaseModel

class VagaDashboard(BaseModel):
    id: int
    titulo: str
    quantidade_candidaturas: int
    aceitas: int
    em_analise: int
    rejeitadas: int


    class Config:
        from_attributes = True