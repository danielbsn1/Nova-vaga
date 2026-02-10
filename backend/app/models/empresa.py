from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class Empresa(Base):
    __tablename__ = "empresas"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True)
    nome = Column(String, nullable=False)
    cnpj = Column(String, unique=True)
    descricao = Column(String)
    
    user = relationship("User")
    vagas = relationship("Vaga", back_populates="empresa")
