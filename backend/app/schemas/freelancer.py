from pydantic import BaseModel

class FreelancerBase(BaseModel):
    nome: str
    cpf: str
    telefone: str | None = None
    habilidades: str | None = None

class FreelancerCreate(FreelancerBase):
    pass

class FreelancerResponse(FreelancerBase):
    id: int
    user_id: int

    class Config:
        from_attributes = True
