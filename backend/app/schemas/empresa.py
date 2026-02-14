from pydantic import BaseModel
from pydantic import BaseModel, EmailStr

class EmpresaBase(BaseModel):
    nome: str
    cnpj: str
    descricao: str | None = None

class EmpresaCreate(EmpresaBase):
    pass

class EmpresaResponse(EmpresaBase):
    id: int
    user_id: int

    class Config:
        from_attributes = True

class registerEmpresa(BaseModel):
    email: EmailStr
    password: str
    profile: EmpresaBase
